#!/usr/bin/env python3

#!/usr/bin/env python3

from bs4 import BeautifulSoup
from nbconvert import HTMLExporter
import nbformat
from pathlib import Path
import argparse
import os

def convert_to_html(notebook_path: Path) -> str:
	notebook = nbformat.read(notebook_path, as_version=4)
	exporter = HTMLExporter()
	body, _ = exporter.from_notebook_node(notebook)
	return body

def strip_hidden_code_cells_from_html(html_content: str) -> str:
	soup = BeautifulSoup(html_content, "html.parser")
	removed = 0
	for input_block in soup.select('.jp-InputArea'):
		pre = input_block.find('pre')
		if pre and pre.text.strip().startswith('#hide'):
			# print(f"Removing input block:\n{pre.text.strip().splitlines()[0]}")
			input_block.decompose()
			removed += 1
	print(f"Done. Removed {removed} code blocks starting with #hide.")
	return str(soup)

def export_clean_html(ipynb_path: Path):
	html_output_dir = ipynb_path.parent.parent / "htmls"
	html_output_dir.mkdir(parents=True, exist_ok=True)
	output_path = html_output_dir / f"{ipynb_path.stem}.html"
	
	print(f"Converting notebook: {ipynb_path}")
	html = convert_to_html(ipynb_path)
	cleaned_html = strip_hidden_code_cells_from_html(html)
	
	with open(output_path, "w", encoding="utf-8") as f:
		f.write(cleaned_html)
		
	print(f"Final HTML saved to: {output_path.resolve()}")
	
if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Convert .ipynb to HTML and strip #hide code inputs")
	parser.add_argument("-i", "--input", type=str, required=True, help="Path to .ipynb file")
	args = parser.parse_args()
	export_clean_html(Path(args.input))
	
	