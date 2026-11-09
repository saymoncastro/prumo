"""Referências de auditoria, sem integração com produto ou rede.

O = reprodução operacional; M = dispositivo/metodologia identificado;
H = hipótese declarada. Aprovar O não certifica M nem vigência atual.
"""
import json
import unittest
from datetime import date, timedelta
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

REF = json.loads(Path(__file__).with_name('referencias.json').read_text())
D = lambda x: Decimal(str(x))
CICLOS = {x['row']: x for x in REF['cycles']}


def precos_operacionais(parametros=None):
    p = REF['parameters'] if parametros is None else parametros
    funcionamento = (D(p['D4']) - D(p['D5'])) * D(p['D6'])
    denominador = sum(D(p[f'D{i}']) * D(p[f'E{i}']) for i in range(9, 13))
    base = funcionamento / denominador if denominador else D(0)
    return {'PRESENCIAL': base, 'EAD': base * D('.25') / 4,
            'EAD FP': base * D('.8'), 'EAD MOOC': D(0)}


def mt_literal_n2(c, agro):
    """Anexo N2 pp.122–123, CHM fornecida, sem inferir cadastro.

    Não usa AC, AA, Z ou auxiliares. Agro é entrada identificada fora de B!L.
    N2 fala em três anos; 1095 dias aqui segue cabeçalho de C5, não
    resolução jurídica de aniversário bissexto. Testar limite separadamente.
    """
    inicio, fim = (date.fromisoformat(c[k]) for k in ['P', 'Q'])
    t0, t1 = (date.fromisoformat(k) for k in REF['period'])
    duracao, periodo = (fim - inicio).days + 1, (t1 - t0).days + 1
    if duracao <= 0:
        raise ValueError('Ciclo inválido')
    fech = (D(c['U']) * 365 / duracao if duracao > 365 else D(c['S'])) / 800
    if fim < t0:
        # Limite de 1.095 dias de C5; não é a exceção FIC R=Q de B.
        quantidade = D(c['Y']) / 2 if (t0-fim).days <= 1095 else D(0)
        feda = D('.5')
    else:
        dias = max(0, (min(fim, t1) - max(inicio, t0)).days + 1)
        quantidade, feda = D(c['Y']), D(dias) / periodo
    return fech * feda * quantidade * D(c['W']) * (D('1.5') if agro else 1)


def quatro_casas(x):
    """Convenção de comparação, NÃO regra oficial de resíduos/precisão."""
    return x.quantize(D('.0001'), rounding=ROUND_HALF_UP)


def peso(valor, limites, pesos):
    for limite, p in zip(limites, pesos):
        if valor < limite:
            return p
    return pesos[-1]


def normalizar(valores):
    total = sum(valores)
    if total <= 0:
        # Validação proposta para cenário; N2 não define redistribuição zero.
        raise ValueError('Denominador sem distribuição definida')
    return [v / total for v in valores]


class Operacional(unittest.TestCase):
    def test_O01_precos(self):
        precos = precos_operacionais()
        for categoria, celula in [('PRESENCIAL','D14'),('EAD','D15'),('EAD FP','D16')]:
            self.assertAlmostEqual(float(precos[categoria]), REF['parameters'][celula], places=9)
        self.assertEqual((precos['EAD'] / precos['PRESENCIAL']).quantize(D('.00000001')), D('.06250000'))
        zeros = REF['parameters'].copy()
        zeros.update({f'D{i}': 0 for i in range(9,13)})
        self.assertEqual(set(precos_operacionais(zeros).values()), {D(0)})

    def test_O02_classificacao_literal(self):
        externo = ['APRENDA MAIS','E-TEC','MEDIOTEC','OUTROS RECURSOS EXTERNOS',
                   'PROGRAMA EJA INTEGRADA - EPT  (SEB/MEC)','UAB']
        mapa = {('EDUCAÇÃO A DISTÂNCIA', f): 'EAD' for f in externo}
        # Usar grafia efetiva do arquivo, não normalização silenciosa.
        modalidade = CICLOS[281]['F']
        mapa = {(modalidade, f): v for (_, f), v in mapa.items()}
        mapa[(modalidade,'SEM PROGRAMA ASSOCIADO')] = 'EAD FP'
        mapa[(modalidade,'OUTROS MOOC')] = 'EAD MOOC'
        presencial = CICLOS[7]['F']
        for financiamento in ['MEDIOTEC','OUTROS RECURSOS EXTERNOS',
                              'PROGRAMA EJA INTEGRADA - EPT  (SEB/MEC)',
                              'SEM PROGRAMA ASSOCIADO']:
            mapa[(presencial,financiamento)] = 'PRESENCIAL'
        for r in CICLOS:
            c=CICLOS[r]
            self.assertEqual(mapa[(c['F'],c['G'])],c['AG'])
        with self.assertRaises(KeyError):
            mapa[(modalidade,'FINANCIAMENTO NÃO CADASTRADO')]

    def test_O03_monetizacao_por_ciclo(self):
        precos=precos_operacionais()
        for c in CICLOS.values():
            self.assertAlmostEqual(float(precos[c['AG']]*D(c['AC'])), c['AE'], places=7)

    def test_O04_totalizacao_campi_e_instituicao(self):
        for col in ['Y','AA','AC','AE']:
            soma=sum(D(x[col]) for x in REF['campus'].values())
            self.assertAlmostEqual(float(soma),REF['totals'][col],places=6)
        self.assertEqual(len(REF['campus']),22)
        self.assertAlmostEqual(sum(CICLOS[r]['AE'] for r in [7,8,9]),REF['agronomia_curso'],places=7)

    def test_O05_denominador_ifes(self):
        c=CICLOS[7]
        self.assertAlmostEqual(c['AE']/REF['totals']['AE'],c['AF'],places=12)
        self.assertNotAlmostEqual(c['AE']/REF['campus'][c['E']]['AE'],c['AF'],places=6)

    def test_O06_icqa_fronteiras(self):
        t0=date(2024,1,1)
        def icqa(q,r): return 0 if r<t0 else (1 if q>=t0 else .5)
        self.assertEqual(icqa(t0,t0),1)
        self.assertEqual(icqa(t0-timedelta(days=1),t0),.5)
        self.assertEqual(icqa(t0-timedelta(days=2),t0-timedelta(days=1)),0)
        for c in CICLOS.values():
            self.assertEqual(icqa(date.fromisoformat(c['Q']),date.fromisoformat(c['R'])),c['Z'])

    def test_O07_ano_bissexto_auxiliar(self):
        self.assertEqual(CICLOS[19]['AO'],366/365)
        self.assertGreater(CICLOS[19]['AO'],1)
        self.assertEqual(REF['formulas']['CICLOS!AO7'],'=(Q7-DATE(YEAR(Q7),1,1)+1)/365')

    def test_O08_mooc_e_diagnostico(self):
        self.assertGreater(CICLOS[99]['AC'],0)
        self.assertEqual(CICLOS[99]['AE'],0)
        self.assertEqual(CICLOS[57]['AE'],0)
        self.assertGreater(CICLOS[57]['AI'],0)
        self.assertEqual(CICLOS[57]['Z'],0)


class MetodoIdentificado(unittest.TestCase):
    def test_M01_mt_amostras_sem_AC(self):
        # Agro validado no cadastro C6 por nome/tipo/eixo unívocos;
        # cadastro é PLOA2025 e não homologa a edição de B.
        for r,agro in [(7,True),(9,True),(11,False),(45,True),(57,False),
                       (173,False),(191,False),(281,False),(380,False),(381,False),(483,False),(573,False)]:
            with self.subTest(row=r):
                c=CICLOS[r].copy()
                esperado=D(c.pop('AC'))
                self.assertEqual(quatro_casas(mt_literal_n2(c,agro)),esperado)

    def test_M02_contraexemplos_nao_sao_conformidade(self):
        # Divergências são resultados da auditoria, não falhas toleradas.
        for r in [99,284,511,585,586]:
            self.assertNotEqual(quatro_casas(mt_literal_n2(CICLOS[r],False)),D(CICLOS[r]['AC']))
        self.assertEqual(quatro_casas(mt_literal_n2(CICLOS[99],False)),D('.0148'))
        self.assertEqual(D(CICLOS[99]['AC']),D('.175'))

    def test_M03_tabelas_continuas_n2(self):
        self.assertEqual([peso(x,[18,20,22],[0,1,2,2.5]) for x in [17.999,18,19.999,20,22,101]], [0,1,1,2,2.5,2.5])
        self.assertEqual([peso(x,[.5,.6],[0,1,2]) for x in [.49,.5,.6]],[0,1,2])
        self.assertEqual([peso(x,[.1,.15,.2],[0,1,2,2.5]) for x in [.09,.1,.15,.2]],[0,1,2,2.5])
        self.assertEqual([peso(x,[.025,.05,.1],[0,1,2,2.5]) for x in [0,.025,.05,.1]],[0,1,2,2.5])

    def test_M04_iea_tabela_e_equacao_divergem(self):
        m=D('.5')
        limites=[D('.9')*m,m,D('1.1')*m,D('1.2')*m]
        self.assertEqual([peso(x,limites,[D('.5'),1,D('1.5'),2,D('2.5')]) for x in [D('.4'),D('.45'),D('.5'),D('.55'),D('.6')]], [D('.5'),1,D('1.5'),2,D('2.5')])
        ponderado_tabela=D('.4')*D('.5')
        ramo_literal_equacao=D('.5')
        self.assertNotEqual(ponderado_tabela,ramo_literal_equacao)

    def test_M05_retencao_duas_metades(self):
        c=CICLOS[11]
        dur=(date.fromisoformat(c['Q'])-date.fromisoformat(c['P'])).days+1
        fech=D(c['U'])*365/dur/800
        self.assertEqual(quatro_casas(fech*D(c['Y'])*D('.5')*D('.5')*D(c['W'])),D(c['AC']))

    def test_M06_ae_rip_e_exemplos_c5(self):
        referencia=D(119)/D(7812)*D('46811139.0126')
        self.assertAlmostEqual(float(referencia),713072.9061,places=4)
        presencial=D('3943.4816')*D('1.7611')/D('1082173.5063')*D('531089605.14')
        self.assertAlmostEqual(float(presencial),3408275.869,places=3)
        self.assertEqual(sum(normalizar([D(119),D('437.5'),D(80)])),D(1))


class Hipoteses(unittest.TestCase):
    def test_H01_participacao_muda_denominador(self):
        self.assertEqual(normalizar([D(20),D(80)])[0],D('.2'))
        self.assertEqual(normalizar([D(30),D(80)])[0],D(30)/110)
        self.assertEqual(normalizar([D(40),D(160)])[0],D('.2'))

    def test_H02_qualidade_fecha_com_submontantes(self):
        iea=normalizar([D('.75'),D('1.5')]);rap=normalizar([D(40),D(55)])
        legal=normalizar([D(1),D(3)])
        valores=[D(100)*(D('.25')*iea[i]+D('.25')*rap[i]+D('.5')*legal[i]) for i in range(2)]
        self.assertEqual(sum(valores),D(100))

    def test_H03_renda_denominador_declarantes(self):
        # Exemplo fictício: 10 não declarantes, declarantes 1/2 em cada
        # faixa de peso 2,5 e 0. A média não usa os não declarantes.
        vr=(D(5)*D('2.5')+D(5)*0)/10
        self.assertEqual(vr,D('1.25'))
        indices=[D(100)*vr,D(50)*D(2)]
        self.assertEqual(sum(normalizar(indices)),D(1))

    def test_H04_zeros_e_precisao_explicitos(self):
        with self.assertRaises(ValueError): normalizar([D(0),D(0)])
        self.assertEqual(quatro_casas(D('1.40625')),D('1.4063'))
        self.assertEqual(quatro_casas(D('1.40624')),D('1.4062'))
        # Mostrar duas casas não significa arredondar cada parcela antes da soma.
        self.assertNotEqual(round(D('.004'),2)*3,round(D('.004')*3,2))

    def test_H05_deficit_nacional_condicional_ead(self):
        p=REF['parameters'];precos=precos_operacionais()
        falta=precos['PRESENCIAL']*D(p['D10'])*(D('.25')-D('.0625'))
        self.assertAlmostEqual(float(falta),15172836.940377317,places=6)
        # Só se as MT nacionais forem comparáveis às MT monetizadas de B.
        distribuido=sum(D(p[f'D{i}'])*precos[k] for i,k in [(9,'PRESENCIAL'),(10,'EAD'),(11,'EAD MOOC'),(12,'EAD FP')])
        self.assertAlmostEqual(float(D(p['D7'])-distribuido),float(falta),places=6)


if __name__ == '__main__':
    unittest.main()
