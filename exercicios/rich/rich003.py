from rich import print
from rich.table import Table

tabela = Table(title="Tabela de Preços")

tabela.add_column("Nome", justify="center", style="cyan")
tabela.add_column("Preço", justify="center", style="red")
tabela.add_row("Lapis", "1,50")
tabela.add_row("Borracha", "[green]3,50")

print(tabela)