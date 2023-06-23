import populars as p
import os

melhores_medias = p.populares()
piores_medias = p.populares(decrescente=True, qtd_minima_avaliacoes=1)
mais_visualizados = p.populares(filtrar_por='visualizacoes')
menos_visualizados = p.populares(filtrar_por='visualizacoes', decrescente=True, qtd_minima_avaliacoes=1)
mais_avaliados = p.populares(filtrar_por='mais_avaliados')
menos_avaliados = p.populares(filtrar_por='mais_avaliados', decrescente=True, qtd_minima_avaliacoes=1)

path = os.path.expanduser("static\csv")

# salva os dataframes como arquivos CSV em path
melhores_medias.to_csv(os.path.join(path, "melhores_medias.csv"), index=False)
piores_medias.to_csv(os.path.join(path, "piores_medias.csv"), index=False)
mais_visualizados.to_csv(os.path.join(path, "mais_visualizados.csv"), index=False)
menos_visualizados.to_csv(os.path.join(path, "menos_visualizados.csv"), index=False)
mais_avaliados.to_csv(os.path.join(path, "mais_avaliados.csv"), index=False)
menos_avaliados.to_csv(os.path.join(path, "menos_avaliados.csv"), index=False)