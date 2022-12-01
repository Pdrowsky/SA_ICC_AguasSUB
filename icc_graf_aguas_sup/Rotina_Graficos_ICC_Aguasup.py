# -*- coding: utf-8 -*-
"""
Created on Mon May 31 21:44:19 2021

@author: Thiago
"""

import matplotlib.pyplot as plt
from extrair_dados.dados_sup import *
import numpy as np
from matplotlib.dates import DayLocator, HourLocator, DateFormatter, drange
import matplotlib.gridspec as gridspec

diretorio_graficos = os.chdir(r'P:\PETROBRAS-0902-ICC-Qualidade da Água 2021\BancoDados\Figuras\AguaSup\Cteste')

class RotinaGraficosSup:
    def __init__(self):
        pass

    def definir_diretorio(self):
        diretorio_graficos = os.chdir(
            r'P:\PETROBRAS-0902-ICC-Qualidade da Água 2021\BancoDados\Figuras\AguaSup\Cteste')

    def plotar_base(self):
        # Plota gráficos OD
        ax = dados_od.iloc[:, 1:13].plot(subplots=True, layout=(12, 3),
                                         figsize=(20, 40),
                                         style=['.-', '.-', '.-', '.-', '.-',
                                                '.-', '.-', '.-', '.-', '.-',
                                                '.-', '.-'], ylabel='OD (mg/L)')
        plt.savefig('Serie_od1.png', bbox_inches='tight')
        plt.close()
        ax = dados_od.iloc[:, 14:22].plot(subplots=True, layout=(12, 3),
                                          figsize=(20, 40),
                                          style=['.-', '.-', '.-', '.-', '.-',
                                                 '.-', '.-', '.-', '.-', '.-',
                                                 '.-', '.-'],
                                          ylabel='OD (mg/L)')
        plt.savefig('Serie_od2.png', bbox_inches='tight')
        plt.close()

        # Plota gráficos Condutividade
        ax = dados_condutiv.iloc[:, 1:13].plot(subplots=True, layout=(12, 3),
                                               figsize=(20, 40),
                                               style=['.-', '.-', '.-', '.-',
                                                      '.-', '.-', '.-', '.-',
                                                      '.-', '.-', '.-', '.-'],
                                               ylabel='Condutividade Elétrica (µS/cm)')
        plt.savefig(
            'Serie_condutiv1.png',
            bbox_inches='tight')
        plt.close()
        ax = dados_condutiv.iloc[:, 14:22].plot(subplots=True, layout=(12, 3),
                                                figsize=(20, 40),
                                                style=['.-', '.-', '.-', '.-',
                                                       '.-', '.-', '.-', '.-',
                                                       '.-', '.-', '.-', '.-'],
                                                ylabel='Condutividade Elétrica (µS/cm)')
        plt.savefig(
            'Serie_condutiv2.png',
            bbox_inches='tight')
        plt.close()

        # Plota gráficos Alumínio
        ax = dados_aluminio.iloc[:, 1:13].plot(subplots=True, layout=(12, 3),
                                               figsize=(20, 40),
                                               style=['.-', '.-', '.-', '.-',
                                                      '.-', '.-', '.-', '.-',
                                                      '.-', '.-', '.-', '.-'],
                                               ylabel='Alumínio (mg/L)')
        plt.savefig(
            'Serie_Aluminio1.png',
            bbox_inches='tight')
        plt.close()
        ax = dados_aluminio.iloc[:, 14:22].plot(subplots=True, layout=(12, 3),
                                                figsize=(20, 40),
                                                style=['.-', '.-', '.-', '.-',
                                                       '.-', '.-', '.-', '.-',
                                                       '.-', '.-', '.-', '.-'],
                                                ylabel='Alumínio (mg/L)')
        plt.savefig(
            'Serie_Aluminio2.png',
            bbox_inches='tight')
        plt.close()

        # Plota gráficos Ferro
        ax = dados_ferro.iloc[:, 1:13].plot(subplots=True, layout=(12, 3),
                                            figsize=(20, 40),
                                            style=['.-', '.-', '.-', '.-', '.-',
                                                   '.-', '.-', '.-', '.-', '.-',
                                                   '.-', '.-'],
                                            ylabel='Ferro (mg/L)')
        plt.savefig(
            'Serie_ferro1.png',
            bbox_inches='tight')
        plt.close()
        ax = dados_ferro.iloc[:, 14:22].plot(subplots=True, layout=(12, 3),
                                             figsize=(20, 40),
                                             style=['.-', '.-', '.-', '.-',
                                                    '.-', '.-', '.-', '.-',
                                                    '.-', '.-', '.-', '.-'],
                                             ylabel='Ferro (mg/L)')
        plt.savefig(
            'Serie_ferro2.png',
            bbox_inches='tight')
        plt.close()

        # Plota gráficos Manganes
        ax = dados_manganes.iloc[:, 1:13].plot(subplots=True, layout=(12, 3),
                                               figsize=(20, 40),
                                               style=['.-', '.-', '.-', '.-',
                                                      '.-', '.-', '.-', '.-',
                                                      '.-', '.-', '.-', '.-'],
                                               ylabel='Manganês (mg/L)')
        plt.savefig(
            'Serie_manganes1.png',
            bbox_inches='tight')
        plt.close()
        ax = dados_manganes.iloc[:, 14:22].plot(subplots=True, layout=(12, 3),
                                                figsize=(20, 40),
                                                style=['.-', '.-', '.-', '.-',
                                                       '.-', '.-', '.-', '.-',
                                                       '.-', '.-', '.-', '.-'],
                                                ylabel='Manganês (mg/L)')
        plt.savefig(
            'Serie_manganes2.png',
            bbox_inches='tight')
        plt.close()

        # Plota gráficos Acidez
        ax = dados_acidez.iloc[:, 1:13].plot(subplots=True, layout=(12, 3),
                                             figsize=(20, 40),
                                             style=['.-', '.-', '.-', '.-',
                                                    '.-', '.-', '.-', '.-',
                                                    '.-', '.-', '.-', '.-'],
                                             ylabel='Acidez Total (mg/L)')
        plt.savefig(
            'Serie_acidez1.png',
            bbox_inches='tight')
        ax = dados_acidez.iloc[:, 14:22].plot(subplots=True, layout=(12, 3),
                                              figsize=(20, 40),
                                              style=['.-', '.-', '.-', '.-',
                                                     '.-', '.-', '.-', '.-',
                                                     '.-', '.-', '.-', '.-'],
                                              ylabel='Acidez Total (mg/L)')
        plt.savefig(
            'Serie_acidez2.png',
            bbox_inches='tight')

        # Plota gráficos Sulfato
        ax = dados_sulfato.iloc[:, 1:13].plot(subplots=True, layout=(12, 3),
                                              figsize=(20, 40),
                                              style=['.-', '.-', '.-', '.-',
                                                     '.-', '.-', '.-', '.-',
                                                     '.-', '.-', '.-', '.-'],
                                              ylabel='Sulfato (mg/L)')
        plt.savefig(
            'Serie_sulfato1.png',
            bbox_inches='tight')
        ax = dados_sulfato.iloc[:, 14:22].plot(subplots=True, layout=(12, 3),
                                               figsize=(20, 40),
                                               style=['.-', '.-', '.-', '.-',
                                                      '.-', '.-', '.-', '.-',
                                                      '.-', '.-', '.-', '.-'],
                                               ylabel='Sulfato (mg/L)')
        plt.savefig(
            'Serie_sulfato2.png',
            bbox_inches='tight')

        # Plota gráficos pH
        ax = dados_ph.iloc[:, 1:13].plot(subplots=True, layout=(12, 3),
                                         figsize=(20, 40),
                                         style=['.-', '.-', '.-', '.-', '.-',
                                                '.-', '.-', '.-', '.-', '.-',
                                                '.-', '.-'], ylabel='pH')
        plt.savefig(
            'Serie_pH1.png',
            bbox_inches='tight')
        ax = dados_ph.iloc[:, 14:22].plot(subplots=True, layout=(12, 3),
                                          figsize=(20, 40),
                                          style=['.-', '.-', '.-', '.-', '.-',
                                                 '.-', '.-', '.-', '.-', '.-',
                                                 '.-', '.-'], ylabel='pH')
        plt.savefig(
            'Serie_pH2.png',
            bbox_inches='tight')

    def plotar_principais_conjunto(self):
        # Plota Gráfico principais poços dos conjuntos - Alumínio
        ASIC1_al = dados_aluminio['ASIC1']
        ASIC10_al = dados_aluminio['ASIC10']
        ASICteste_al = dados_aluminio['ASIC3/4']
        ASIC2_al = dados_aluminio['ASIC2']
        ASIC17_al = dados_aluminio['ASIC 17']

        fig, ax = plt.subplots()
        # ax.xaxis.set_major_formatter(DateFormatter('%d/%m/%Y'))
        ax.plot(ASIC1_al, '.-', label='ASIC1')
        ax.plot(ASIC2_al, '.-', label='ASIC2')
        ax.plot(ASIC10_al, '.-', label='ASIC10')
        ax.plot(ASICteste_al, '.-', label='ASIC3/4')
        ax.plot(ASIC17_al, '.-', label='ASIC 17')

        leg = ax.legend()
        # ax.set_yscale('log')
        # plt.legend(loc = "upper right")
        ax.set(xlabel='Ano', ylabel='Alumínio (mg/L)')
        ax.grid()
        plt.savefig(
            'Conjuntos_aluminio.png',
            bbox_inches='tight', dpi=300)

        # Plota Gráfico principais poços dos conjuntos - Ferro
        ASIC1_fe = dados_ferro['ASIC1']
        ASIC10_fe = dados_ferro['ASIC10']
        ASICteste_fe = dados_ferro['ASIC3/4']
        ASIC2_fe = dados_ferro['ASIC2']
        ASIC17_fe = dados_ferro['ASIC 17']

        fig, ax = plt.subplots()
        # ax.xaxis.set_major_formatter(DateFormatter('%d/%m/%Y'))
        ax.plot(ASIC1_fe, '.-', label='ASIC1')
        ax.plot(ASIC2_fe, '.-', label='ASIC2')
        ax.plot(ASIC10_fe, '.-', label='ASIC10')
        ax.plot(ASICteste_fe, '.-', label='ASIC3/4')
        ax.plot(ASIC17_fe, '.-', label='ASIC 17')
        leg = ax.legend()

        ax.set(xlabel='Ano', ylabel='Ferro Total(mg/L)')
        ax.grid()

        plt.savefig(
            'Conjuntos_ferro.png',
            bbox_inches='tight', dpi=300)

        # Plota Gráfico principais poços dos conjuntos - Manganês
        ASIC1_mg = dados_manganes['ASIC1']
        ASIC10_mg = dados_manganes['ASIC10']
        ASICteste_mg = dados_manganes['ASIC3/4']
        ASIC2_mg = dados_manganes['ASIC2']
        ASIC17_mg = dados_manganes['ASIC 17']

        fig, ax = plt.subplots()
        # ax.xaxis.set_major_formatter(DateFormatter('%d/%m/%Y'))
        ax.plot(ASIC1_mg, '.-', label='ASIC1')
        ax.plot(ASIC2_mg, '.-', label='ASIC2')
        ax.plot(ASIC10_mg, '.-', label='ASIC10')
        ax.plot(ASICteste_mg, '.-', label='ASIC3/4')
        ax.plot(ASIC17_mg, '.-', label='ASIC 17')
        leg = ax.legend()

        ax.set(xlabel='Ano', ylabel='Manganês Total(mg/L)')
        ax.grid()

        plt.savefig(
            'Conjuntos_manganes.png',
            bbox_inches='tight', dpi=300)

        # Plota Gráfico principais poços dos conjuntos - Acidez
        ASIC1_ac = dados_acidez['ASIC1']
        ASIC10_ac = dados_acidez['ASIC10']
        ASICteste_ac = dados_acidez['ASIC3/4']
        ASIC2_ac = dados_acidez['ASIC2']
        ASIC17_ac = dados_acidez['ASIC 17']

        fig, ax = plt.subplots()
        # ax.xaxis.set_major_formatter(DateFormatter('%d/%m/%Y'))
        ax.plot(ASIC1_ac, '.-', label='ASIC1')
        ax.plot(ASIC2_ac, '.-', label='ASIC2')
        ax.plot(ASIC10_ac, '.-', label='ASIC10')
        ax.plot(ASICteste_ac, '.-', label='ASIC3/4')
        ax.plot(ASIC17_ac, '.-', label='ASIC 17')
        leg = ax.legend()

        ax.set(xlabel='Ano', ylabel='Acidez Total(mg/L)')
        ax.grid()

        plt.savefig(
            'Conjuntos_acidez.png',
            bbox_inches='tight', dpi=300)

        # Plota Gráfico principais poços dos conjuntos - Sulfato
        ASIC1_so = dados_sulfato['ASIC1']
        ASIC10_so = dados_sulfato['ASIC10']
        ASICteste_so = dados_sulfato['ASIC3/4']
        ASIC2_so = dados_sulfato['ASIC2']
        ASIC17_so = dados_sulfato['ASIC 17']

        fig, ax = plt.subplots()
        # ax.xaxis.set_major_formatter(DateFormatter('%d/%m/%Y'))
        ax.plot(ASIC1_so, '.-', label='ASIC1')
        ax.plot(ASIC2_so, '.-', label='ASIC2')
        ax.plot(ASIC10_so, '.-', label='ASIC10')
        ax.plot(ASICteste_so, '.-', label='ASIC3/4')
        ax.plot(ASIC17_so, '.-', label='ASIC 17')
        leg = ax.legend()

        ax.set(xlabel='Ano', ylabel='Sulfato Total(mg/L)')
        ax.grid()

        plt.savefig(
            'Conjuntos_sulfato.png',
            bbox_inches='tight', dpi=300)

        # Plota Gráfico principais poços dos conjuntos - pH
        ASIC1_ph = dados_ph['ASIC1']
        ASIC10_ph = dados_ph['ASIC10']
        ASICteste_ph = dados_ph['ASIC3/4']
        ASIC2_ph = dados_ph['ASIC2']
        ASIC17_ph = dados_ph['ASIC 17']

        fig, ax = plt.subplots()

        # ax.xaxis.set_major_formatter(DateFormatter('%d/%m/%Y'))
        ax.plot(ASIC1_ph, '.-', label='ASIC1')
        ax.plot(ASIC2_ph, '.-', label='ASIC2')
        ax.plot(ASIC10_ph, '.-', label='ASIC10')
        ax.plot(ASICteste_ph, '.-', label='ASIC3/4')
        ax.plot(ASIC17_ph, '.-', label='ASIC 17')
        leg = ax.legend()

        plt.legend(loc="best",
                   ncol=2)  # expand stretches it along the bottom # while ncol specifies the number of columns
        ax.set(xlabel='Ano', ylabel='pH')
        ax.grid()

        plt.savefig(
            'Conjuntos_pH.png',
            bbox_inches='tight', dpi=300)

        # Plota Gráfico principais poços dos conjuntos - Condutividade
        ASIC1_condutiv = dados_condutiv['ASIC1']
        ASIC10_condutiv = dados_condutiv['ASIC10']
        ASICteste_condutiv = dados_condutiv['ASIC3/4']
        ASIC2_condutiv = dados_condutiv['ASIC2']
        ASIC17_condutiv = dados_condutiv['ASIC 17']

        fig, ax = plt.subplots()

        # ax.xaxis.set_major_formatter(DateFormatter('%d/%m/%Y'))
        ax.plot(ASIC1_condutiv, '.-', label='ASIC1')
        ax.plot(ASIC2_condutiv, '.-', label='ASIC2')
        ax.plot(ASIC10_condutiv, '.-', label='ASIC10')
        ax.plot(ASICteste_condutiv, '.-', label='ASIC3/4')
        ax.plot(ASIC17_condutiv, '.-', label='ASIC 17')
        leg = ax.legend()

        plt.legend(loc="best",
                   ncol=2)  # expand stretches it along the bottom # while ncol specifies the number of columns
        ax.set(xlabel='Ano', ylabel='Condutividade Elétrica (µS/cm)')
        ax.grid()

        plt.savefig(
            'Conjuntos_condutiv.png',
            bbox_inches='tight', dpi=300)

    def plotar_cargas(self):
        # Gráficos das Cargas

        ASIC1_cacidez = dados_cargasacidez['ASIC1']
        ASIC10_cacidez = dados_cargasacidez['ASIC10']
        ASICteste_cacidez = dados_cargasacidez['ASIC3/4']
        ASIC2_cacidez = dados_cargasacidez['ASIC2']
        ASIC17_cacidez = dados_cargasacidez['ASIC 17']

        fig, ax = plt.subplots()

        # ax.xaxis.set_major_formatter(DateFormatter('%d/%m/%Y'))

        ax.plot(ASIC1_cacidez, '.-', label='ASIC1')
        ax.plot(ASIC2_cacidez, '.-', label='ASIC2')
        ax.plot(ASIC10_cacidez, '.-', label='ASIC10')
        ax.plot(ASICteste_cacidez, '.-', label='ASIC3/4')
        ax.plot(ASIC17_cacidez, '.-', label='ASIC 17')
        ax.set_yscale('log')
        leg = ax.legend()

        plt.legend(loc="best",
                   ncol=2)  # expand stretches it along the bottom # while ncol specifies the number of columns
        ax.set(xlabel='Ano', ylabel='Carga Acidez (kg/h)')
        ax.grid()

        plt.savefig(
            'Cargas_Acidez.png',
            bbox_inches='tight', dpi=300)

        ASIC1_caluminio = dados_cargasaluminio['ASIC1']
        ASIC10_caluminio = dados_cargasaluminio['ASIC10']
        ASICteste_caluminio = dados_cargasaluminio['ASIC3/4']
        ASIC2_caluminio = dados_cargasaluminio['ASIC2']
        ASIC17_caluminio = dados_cargasaluminio['ASIC 17']

        fig, ax = plt.subplots()

        # ax.xaxis.set_major_formatter(DateFormatter('%d/%m/%Y'))

        ax.plot(ASIC1_caluminio, '.-', label='ASIC1')
        ax.plot(ASIC2_caluminio, '.-', label='ASIC2')
        ax.plot(ASIC10_caluminio, '.-', label='ASIC10')
        ax.plot(ASICteste_caluminio, '.-', label='ASIC3/4')
        ax.plot(ASIC17_caluminio, '.-', label='ASIC 17')
        ax.set_yscale('log')
        plt.legend(loc="lower left")
        leg = ax.legend()

        plt.legend(loc="lower left",
                   ncol=2)  # expand stretches it along the bottom # while ncol specifies the number of columns
        ax.set(xlabel='Ano', ylabel='Carga Alumínio(kg/h)')
        ax.grid()

        plt.savefig(
            'Cargas_Aluminio.png',
            bbox_inches='tight', dpi=300)

        ASIC1_cferro = dados_cargasferro['ASIC1']
        ASIC10_cferro = dados_cargasferro['ASIC10']
        ASICteste_cferro = dados_cargasferro['ASIC3/4']
        ASIC2_cferro = dados_cargasferro['ASIC2']
        ASIC17_cferro = dados_cargasferro['ASIC 17']

        fig, ax = plt.subplots()

        # ax.xaxis.set_major_formatter(DateFormatter('%d/%m/%Y'))

        ax.plot(ASIC1_cferro, '.-', label='ASIC1')
        ax.plot(ASIC2_cferro, '.-', label='ASIC2')
        ax.plot(ASIC10_cferro, '.-', label='ASIC10')
        ax.plot(ASICteste_cferro, '.-', label='ASIC3/4')
        ax.plot(ASIC17_cferro, '.-', label='ASIC 17')
        ax.set_yscale('log')
        leg = ax.legend()

        plt.legend(loc="best",
                   ncol=2)  # expand stretches it along the bottom # while ncol specifies the number of columns
        ax.set(xlabel='Ano', ylabel='Carga Ferro (kg/h)')
        ax.grid()

        plt.savefig(
            'Cargas_Ferro.png',
            bbox_inches='tight', dpi=300)

        ASIC1_cmanganes = dados_cargasmanganes['ASIC1']
        ASIC10_cmanganes = dados_cargasmanganes['ASIC10']
        ASICteste_cmanganes = dados_cargasmanganes['ASIC3/4']
        ASIC2_cmanganes = dados_cargasmanganes['ASIC2']
        ASIC17_cmanganes = dados_cargasmanganes['ASIC 17']

        fig, ax = plt.subplots()

        # ax.xaxis.set_major_formatter(DateFormatter('%d/%m/%Y'))

        ax.plot(ASIC1_cmanganes, '.-', label='ASIC1')
        ax.plot(ASIC2_cmanganes, '.-', label='ASIC2')
        ax.plot(ASIC10_cmanganes, '.-', label='ASIC10')
        ax.plot(ASICteste_cmanganes, '.-', label='ASIC3/4')
        ax.plot(ASIC17_cmanganes, '.-', label='ASIC 17')
        ax.set_yscale('log')
        leg = ax.legend()

        plt.legend(loc="best",
                   ncol=2)  # expand stretches it along the bottom # while ncol specifies the number of columns
        ax.set(xlabel='Ano', ylabel='Carga Manganês (kg/h)')
        ax.grid()

        plt.savefig(
            'Cargas_Manganes.png',
            bbox_inches='tight', dpi=300)

        ASIC1_csulfato = dados_cargassulfato['ASIC1']
        ASIC10_csulfato = dados_cargassulfato['ASIC10']
        ASICteste_csulfato = dados_cargassulfato['ASIC3/4']
        ASIC2_csulfato = dados_cargassulfato['ASIC2']
        ASIC17_csulfato = dados_cargassulfato['ASIC 17']

        fig, ax = plt.subplots()

        # ax.xaxis.set_major_formatter(DateFormatter('%d/%m/%Y'))

        ax.plot(ASIC1_csulfato, '.-', label='ASIC1')
        ax.plot(ASIC2_csulfato, '.-', label='ASIC2')
        ax.plot(ASIC10_csulfato, '.-', label='ASIC10')
        ax.plot(ASICteste_csulfato, '.-', label='ASIC3/4')
        ax.plot(ASIC17_csulfato, '.-', label='ASIC 17')
        ax.set_yscale('log')
        leg = ax.legend()

        plt.legend(loc="best",
                   ncol=2)  # expand stretches it along the bottom # while ncol specifies the number of columns
        ax.set(xlabel='Ano', ylabel='Carga Sulfato (kg/h)')
        ax.grid()

        plt.savefig(
            'Cargas_Sulfato.png',
            bbox_inches='tight', dpi=300)

        acidez = dados_cargasDAM['Acidez']
        aluminio = dados_cargasDAM['Aluminio']
        ferro = dados_cargasDAM['Ferro']
        manganes = dados_cargasDAM['Manganês']
        sulfato = dados_cargasDAM['Sulfato']

        fig, ax = plt.subplots()

        # ax.xaxis.set_major_formatter(DateFormatter('%d/%m/%Y'))

        ax.plot(acidez, '.-', label='Acidez (kg/h)')
        ax.plot(aluminio, '.-', label='Alumínio (kg/h)')
        ax.plot(ferro, '.-', label='Ferro (kg/h)')
        ax.plot(manganes, '.-', label='Manganês (kg/h)')
        ax.plot(sulfato, '.-', label='Sulfato (kg/h)')
        ax.set_yscale('log')
        leg = ax.legend()

        plt.legend(bbox_to_anchor=(1.0, 0.5), loc="center left",
                   ncol=1)  # expand stretches it along the bottom # while ncol specifies the number of columns
        ax.set(xlabel='Ano', ylabel='Cargas (kg/h)')
        ax.grid()

        plt.savefig(
            'Cargas_DAM.png',
            bbox_inches='tight', dpi=300)

    def plotar_multinivel(self):
        # Plota gráfico Conjuntos Multinivel - Alumínio
        PP01S_al = dados_aluminio['PP-01S']
        PP01R_al = dados_aluminio['PP-01R']
        PP02S_al = dados_aluminio['PP-02S']
        PP02R_al = dados_aluminio['PP-02R']

        fig, ax = plt.subplots()
        # ax.xaxis.set_major_formatter(DateFormatter('%d/%m/%Y'))
        ax.plot(PP01S_al, '.-', label='PP-01S')
        ax.plot(PP01R_al, '.-', label='PP-01R')
        ax.plot(PP02S_al, '.-', label='PP-02S')
        ax.plot(PP02R_al, '.-', label='PP-02R')
        ax.set_yscale('log')
        leg = ax.legend()

        ax.set(xlabel='Ano', ylabel='Alumínio Total (mg/L)')
        ax.grid()
        plt.legend(loc="best",
                   ncol=2)  # expand stretches it along the bottom # while ncol specifies the number of columns

        plt.savefig(
            'Multinivel_aluminio.png',
            bbox_inches='tight', dpi=300)

        # Plota gráfico Conjuntos Multinivel - Ferro
        PP01S_fe = dados_ferro['PP-01S']
        PP01R_fe = dados_ferro['PP-01R']
        PP02S_fe = dados_ferro['PP-02S']
        PP02R_fe = dados_ferro['PP-02R']

        fig, ax = plt.subplots()
        # ax.xaxis.set_major_formatter(DateFormatter('%d/%m/%Y'))
        ax.plot(PP01S_fe, '.-', label='PP-01S')
        ax.plot(PP01R_fe, '.-', label='PP-01R')
        ax.plot(PP02S_fe, '.-', label='PP-02S')
        ax.plot(PP02R_fe, '.-', label='PP-02R')

        leg = ax.legend()

        ax.set(xlabel='Ano', ylabel='Ferro Total (mg/L)')
        ax.grid()
        plt.legend(loc="best",
                   ncol=2)  # expand stretches it along the bottom # while ncol specifies the number of columns

        plt.savefig(
            'Multinivel_ferro.png',
            bbox_inches='tight', dpi=300)

        # Plota gráfico Conjuntos Multinivel - Manganês
        PP01S_mg = dados_manganes['PP-01S']
        PP01R_mg = dados_manganes['PP-01R']
        PP02S_mg = dados_manganes['PP-02S']
        PP02R_mg = dados_manganes['PP-02R']

        fig, ax = plt.subplots()
        # ax.xaxis.set_major_formatter(DateFormatter('%d/%m/%Y'))
        ax.plot(PP01S_mg, '.-', label='PP-01S')
        ax.plot(PP01R_mg, '.-', label='PP-01R')
        ax.plot(PP02S_mg, '.-', label='PP-02S')
        ax.plot(PP02R_mg, '.-', label='PP-02R')

        leg = ax.legend()

        ax.set(xlabel='Ano', ylabel='Manganês Total (mg/L)')
        ax.grid()
        plt.legend(loc="best",
                   ncol=2)  # while ncol specifies the number of columns

        plt.savefig(
            'Multinivel_manganes.png',
            bbox_inches='tight', dpi=300)

        # Plota gráfico Conjuntos Multinivel - Acidez
        PP01S_ac = dados_acidez['PP-01S']
        PP01R_ac = dados_acidez['PP-01R']
        PP02S_ac = dados_acidez['PP-02S']
        PP02R_ac = dados_acidez['PP-02R']

        fig, ax = plt.subplots()
        # ax.xaxis.set_major_formatter(DateFormatter('%d/%m/%Y'))
        ax.plot(PP01S_ac, '.-', label='PP-01S')
        ax.plot(PP01R_ac, '.-', label='PP-01R')
        ax.plot(PP02S_ac, '.-', label='PP-02S')
        ax.plot(PP02R_ac, '.-', label='PP-02R')

        leg = ax.legend()

        ax.set(xlabel='Ano', ylabel='Acidez Total (mg/L)')
        ax.grid()
        plt.legend(loc="best",
                   ncol=2)  # while ncol specifies the number of columns

        plt.savefig(
            'Multinivel_acidez.png',
            bbox_inches='tight', dpi=300)

        # Plota gráfico Conjuntos Multinivel - Sulfato
        PP01S_so = dados_sulfato['PP-01S']
        PP01R_so = dados_sulfato['PP-01R']
        PP02S_so = dados_sulfato['PP-02S']
        PP02R_so = dados_sulfato['PP-02R']

        fig, ax = plt.subplots()
        # ax.xaxis.set_major_formatter(DateFormatter('%d/%m/%Y'))
        ax.plot(PP01S_so, '.-', label='PP-01S')
        ax.plot(PP01R_so, '.-', label='PP-01R')
        ax.plot(PP02S_so, '.-', label='PP-02S')
        ax.plot(PP02R_so, '.-', label='PP-02R')

        leg = ax.legend()

        ax.set(xlabel='Ano', ylabel='Sulfato Total (mg/L)')
        ax.grid()
        plt.legend(loc="upper right",
                   ncol=1)  # while ncol specifies the number of columns

        plt.savefig(
            'Multinivel_sulfato.png',
            bbox_inches='tight', dpi=300)

        # Plota gráfico Conjuntos Multinivel - pH
        PP01S_ph = dados_ph['PP-01S']
        PP01R_ph = dados_ph['PP-01R']
        PP02S_ph = dados_ph['PP-02S']
        PP02R_ph = dados_ph['PP-02R']

        fig, ax = plt.subplots()
        # ax.xaxis.set_major_formatter(DateFormatter('%d/%m/%Y'))
        ax.plot(PP01S_ph, '.-', label='PP-01S')
        ax.plot(PP01R_ph, '.-', label='PP-01R')
        ax.plot(PP02S_ph, '.-', label='PP-02S')
        ax.plot(PP02R_ph, '.-', label='PP-02R')

        leg = ax.legend()

        ax.set(xlabel='Ano', ylabel='pH')
        ax.grid()
        plt.legend(loc="best",
                   ncol=2)  # while ncol specifies the number of columns

        plt.savefig(
            'Multinivel_ph.png',
            bbox_inches='tight', dpi=300)

    def plotar_restante(self):
        # Dados por Campanha
        dados_C29 = pd.read_excel(
            r"P:\PETROBRAS\902_ICC_QUALIDADE_DA_AGUA_2021\BancoDados\ICC_AguaSub_Campanhas.xlsx",
            sheet_name='C29')

        pocos = dados_C29['ID POCO']
        ph_c29 = dados_C29[('pH')]

        # fig, ax = plt.subplots()

        fig, ax = plt.subplots(nrows=1, ncols=9, sharey='row', figsize=(40, 10))
        ax[0].bar(pocos[:4], ph_c29[:4], color='#15275c', width=0.5)
        ax[1].bar(pocos[4:7], ph_c29[4:7], color='#4e2d6e', label='Conj. 2',
                  width=0.5)
        ax[2].bar(pocos[7:10], ph_c29[7:10], color='#802f75', label='Conj. 3',
                  width=0.5)
        ax[3].bar(pocos[10:14], ph_c29[10:14], color='#af3271', label='Conj. 4',
                  width=0.5)
        ax[4].bar(pocos[14:16], ph_c29[14:16], color='#d73e63', label='Conj. 5',
                  width=0.5)
        ax[5].bar(pocos[16:17], ph_c29[16:17], color='#f2594e', label='Conj. 6',
                  width=0.5)
        ax[6].bar(pocos[17:20], ph_c29[17:20], color='#ff7d33', label='Conj. 7',
                  width=0.5)
        ax[7].bar(pocos[20:24], ph_c29[20:24], color='#ffa600', label='Conj. 8',
                  width=0.5)
        ax[8].bar(pocos[24:34], ph_c29[24:34], color='#ecff00', label='Conj. 9',
                  width=0.5)

        # ax[0].set_xlim(-2, 8)

        leg = ax[0].legend()
        ax[0].set(ylabel='pH')
        plt.xticks(rotation=45)

        plt.savefig(
            'c29_pH.png',
            bbox_inches='tight', dpi=300)

        plt.show()

        fig5 = plt.figure(figsize=(40, 10))
        widths = [4, 3, 3, 4, 2, 1.5, 3, 4, 10]
        heights = [1]
        spec5 = fig5.add_gridspec(ncols=9, nrows=1, width_ratios=widths,
                                  height_ratios=heights)

        ax1 = fig5.add_subplot(spec5[0, 0])
        ax1.bar(pocos[:4], ph_c28[:4], color='#15275c', width=0.5)
        ax2 = fig5.add_subplot(spec5[0, 1], sharey=ax1)
        plt.setp(ax2.get_yticklabels(), visible=False)
        ax2.bar(pocos[4:7], ph_c28[4:7], color='#4e2d6e', label='Conj. 2',
                width=0.5)
        ax3 = fig5.add_subplot(spec5[0, 2], sharey=ax1)
        plt.setp(ax3.get_yticklabels(), visible=False)
        ax3.bar(pocos[7:10], ph_c28[7:10], color='#802f75', label='Conj. 3',
                width=0.5)
        ax4 = fig5.add_subplot(spec5[0, 3], sharey=ax1)
        plt.setp(ax4.get_yticklabels(), visible=False)
        ax4.bar(pocos[10:14], ph_c28[10:14], color='#af3271', label='Conj. 4',
                width=0.5)
        ax5 = fig5.add_subplot(spec5[0, 4], sharey=ax1)
        plt.setp(ax5.get_yticklabels(), visible=False)
        ax5.bar(pocos[14:16], ph_c28[14:16], color='#d73e63', label='Conj. 5',
                width=0.5)

        ax6 = fig5.add_subplot(spec5[0, 5], sharey=ax1)
        plt.setp(ax6.get_yticklabels(), visible=False)
        ax6.bar(pocos[16:17], ph_c28[16:17], color='#f2594e', label='Conj. 6',
                width=0.1)

        ax7 = fig5.add_subplot(spec5[0, 6], sharey=ax1)
        plt.setp(ax7.get_yticklabels(), visible=False)
        ax7.bar(pocos[17:20], ph_c28[17:20], color='#ff7d33', label='Conj. 7',
                width=0.5)
        ax8 = fig5.add_subplot(spec5[0, 7], sharey=ax1)
        plt.setp(ax8.get_yticklabels(), visible=False)
        ax8.bar(pocos[20:24], ph_c28[20:24], color='#ffa600', label='Conj. 8',
                width=0.5)
        ax9 = fig5.add_subplot(spec5[0, 8], sharey=ax1)
        plt.setp(ax9.get_yticklabels(), visible=False)
        ax9.bar(pocos[24:34], ph_c28[24:34], color='#ecff00', label='Conj. 9',
                width=0.5)
        # plt.show()

        plt.savefig(
            'c28_pH.png',
            bbox_inches='tight', dpi=300)
        plt.close()
