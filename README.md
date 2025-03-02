# Leitor de NF-e em XML

## Descrição
O **Leitor de NF-e em XML** é um projeto desenvolvido em Python para automatizar a extração de informações de Notas Fiscais Eletrônicas (**NF-e**) no formato **XML**. O sistema permite a leitura dos arquivos, extração de dados estruturados e armazenamento em diferentes formatos (CSV, JSON, banco de dados, etc.).

## Funcionalidades
-  **Leitura de arquivos XML** de NF-e.
-  **Extração de informações** como CNPJ, produtos, valores, tributação e totais.
-  **Geração de relatórios** em xmlx.

## Tecnologias Utilizadas
- **Python 3.7+**
- **Bibliotecas**:
  - `openpyxl` (Leitura de XML)
  - `pandas`   (Manipulação de dados e exportação)
  - `Tkinter`   (Interface Gráfica)

## Instalação e Configuração

### 1️⃣ **Clonar o Repositório**
```bash
git clone "link"
	cd leitor-nfe
```

### 2️⃣ **Criar um Ambiente Virtual (Opcional, mas Recomendado)**
```bash
	python -m venv venv
# Ativar o ambiente virtual
# No Windows:
	venv\Scripts\activate
# No Linux/Mac:
	source venv/bin/activate
```

### 3️⃣ **Instalar Dependências**
```bash
pip install -r requirements.txt
```

## Como Usar
### **Executar a Leitura de NF-e**
```bash
python main.py --arquivo "caminho/para/nota.xml"
```
### **Exportar para XMLX**
```bash
python main.py --arquivo "nota.xml" --saida "Notafiscal.xmlx"
```

## Estrutura do Projeto
```
 NF-e reader/
 │── data/                # Pasta para armazenar os XMLs processados
 │── input/               # Pasta para armazenar os XMLs para processar
 │── output/              # Saída de CSV, Excel ou JSON
 │── src/                 # Código-fonte do projeto
 │   ├── reader.py        # Função de leitura dos arquivos XML
 │   ├── nf_data.py       # Estrutura para armazenamento
 │   ├── move_files.py    # Função para mover os arquivos XML
 │   ├── get_paths.py     # Função de leitura do XML
 │   ├── mainwindow.py    # Janela da aplicação
 │   ├── info_nfs.py      # Função para obter as informações
 │── requirements.txt     # Dependências do projeto
 │── README.md            # Documentação
```

## Licença
Este projeto está licenciado sob a **MIT License** - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## Contribuição
Contribuições são bem-vindas! Siga estes passos:
1. **Fork** o repositório
2. Crie uma **branch** para sua funcionalidade (`git checkout -b minha-feature`)
3. Faça o **commit** das suas mudanças (`git commit -m 'Adiciona nova feature'`)
4. Envie para o repositório (`git push origin minha-feature`)
5. Abra um **Pull Request**
---

**Leitor de NF-e** - Automatize o processamento das suas notas fiscais de forma simples!

