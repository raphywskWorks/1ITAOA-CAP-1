options(repos = c(CRAN = "https://cran.r-project.org/"))
install.packages("dplyr")
library(dplyr)

cat('\014')

caminho_atual <- getwd()
arquivo_csv <- file.path(caminho_atual, "dados.csv")

if (!file.exists(arquivo_csv)) {
  cat("Dados não encontrados\n")
  quit(status = 1)  # Encerra o script
}

dados <- read.csv(arquivo_csv, sep = ',', header = TRUE, stringsAsFactors = FALSE)

if (nrow(dados) == 0) {
  cat("Dados não encontrados\n")
  quit(status = 1)
}

dados$totalArea <- as.numeric(dados$totalArea)
dados$plantingArea <- as.numeric(dados$plantingArea)
dados$productQtd <- as.numeric(dados$productQtd)

resultado <- dados %>%
  group_by(culture) %>%
  summarise(
    media_totalArea = mean(totalArea, na.rm = TRUE),
    mediana_totalArea = median(totalArea, na.rm = TRUE),
    desvio_totalArea = sd(totalArea, na.rm = TRUE),
    media_plantingArea = mean(plantingArea, na.rm = TRUE),
    mediana_plantingArea = median(plantingArea, na.rm = TRUE),
    desvio_plantingArea = sd(plantingArea, na.rm = TRUE),
    media_productQtd = mean(productQtd, na.rm = TRUE),
    mediana_productQtd = median(productQtd, na.rm = TRUE),
    desvio_productQtd = sd(productQtd, na.rm = TRUE)
  )

print(resultado)
