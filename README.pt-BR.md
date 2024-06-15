![Static Badge](https://img.shields.io/badge/python-3.9%20%7C%203.10%20%7C%203.11-blue)
![Static Badge](https://img.shields.io/badge/vers%C3%A3o-v0.2.0-orange?logo=github)

_Leia em outros idiomas: [en-US](https://github.com/jvcarli/femder/blob/main/README.md),
[pt-BR](https://github.com/jvcarli/femder/blob/main/README.pt-BR.md)_

# femder

Código de Método de Elementos Finitos (FEM) para acústica escrito para o curso
de graduação "Métodos Numéricos em Acústica e Vibrações", ministrado por Dr. Paulo Mareze.

## Reconhecimento

**Autor original**: Luiz Augusto T. Ferraz Alvim <br/>
**Co-autor original**: Dr. Paulo Mareze

Esse repositório inicialmente era um _fork_ de
[gutoalvim/femder](https://github.com/gutoalvim/femder/), porém foi desacoplado.
Ele compartilha código desde o primeiro commit do seu parente até
[gutoalvim/femder@`16a7231`](https://github.com/gutoalvim/femder/commit/16a7231).
A partir de [jvcarli/femder@`a447e21`](https://github.com/jvcarli/femder/commit/a447e21)
eles divergem.

## Instalação

Pré-requisitos:

- Python >= 3.9, < 3.12

**Obs.**: Se você é iniciante em programação recomendamos fortemente que
siga o guia de instalação para o conda abaixo e baixe a
[Distribuição Anaconda (_Anaconda Distribution_)](https://www.anaconda.com/download) - ela inclui
Python, [NumPy](https://github.com/numpy/numpy), muitos outros pacotes comumente usados
para computação científica e
o [conda](https://docs.conda.io/en/latest/) - um
[gerenciador de pacotes](https://pt.wikipedia.org/wiki/Sistema_gestor_de_pacotes)
que facilita a instalação e gestão de outros pacotes que você pode precisar.

**Siga as instruções abaixo**:

<details>

<summary>Para o <a href="https://docs.conda.io"><code>conda</code></a> - um gerenciador de pacotes que vem com <a href="https://www.anaconda.com/download">Anaconda Distribution</a>, <a href="https://docs.anaconda.com/free/miniconda/">Miniconda</a> e <a href="https://github.com/conda-forge/miniforge">Miniforge</a> (<em>clique para expandir</em>):</summary>

- Você precisará de uma [_shell_](https://pt.wikipedia.org/wiki/Shell_(computa%C3%A7%C3%A3o))
com o `conda` em seu <code><a href="https://pt.wikipedia.org/wiki/Caminho_(computa%C3%A7%C3%A3o)">caminho <em>(PATH)</em></a></code>.

  Se você usa o Windows e instalou Anaconda Distribution, Miniconda, ou Miniforge,
  terá acesso aos programas **`Anaconda Prompt`**,
  **`Anaconda Prompt (miniconda3)`**, ou **`Miniforge Prompt`**, respectivamente.
  Procure por eles no menu iniciar do Windows.

- Crie e ative seu ambiente (_environment_) `conda`:

  É uma boa prática criar um novo `conda` _environment_ para cada projeto em
  que você trabalha. Isso propicia um melhor gerenciamento e isolamento de dependências
  e promove um fluxo de trabalho mais limpo.

  Você **DEVE** usar Python >= 3.9, < 3.12.

  ```
  conda create -n meuenv python=3.9
  conda activate meuenv
  ```

- Instale o `femder` usando o `pip`:

  ```
  pip install femder
  ```

</details>

<details>

<summary>Para o <a href="https://pip.pypa.io/en/stable/getting-started/"><code>pip</code></a> - um gerenciador de pacotes que vem com o Python (<em>clique para expandir</em>):</summary>

- Etapa opcional (**recomendado**) - considere usar um [ambiente virtual (_virtual environment_)](https://docs.python.org/pt-br/3/library/venv.html):

  É uma boa prática criar um novo _virtual environment_ para cada projeto em
  que você trabalha. Isso propicia um melhor gerenciamento e isolamento de dependências
  e promove um fluxo de trabalho mais limpo.

  - Crie seu _virtual environment_ como de costume:

    ```
    python -m venv venv
    ```

  - Ative o _virtual environment_:

    - Se você usa o Windows:

      ```
      .\venv\Scripts\activate
      ```

    - Se você usa o macOS ou uma distribuição Linux:

      ```
      source venv/bin/activate
      ```

- Instale o `femder` usando o `pip`:

  ```
  pip install femder
  ```

</details>

## Exemplos

Para instruções de como executar os exemplos,
olhe o arquivo [README (**em inglês**)](https://github.com/jvcarli/femder/tree/main/examples) no
diretório `examples`.

## Contribuindo

Obrigado por considerar contribuir com o `femder`!
Você pode contribuir como usuário ou desenvolvedor,
por favor leia nosso [guia de contribuição (**em inglês**)](https://github.com/jvcarli/femder/blob/main/CONTRIBUTING.md).

Lembre-se, nenhuma contribuição é pequena demais! Cada linha de código, atualização de documentação,
e relatório de _bug_ ajuda a tornar a biblioteca melhor para todos.

---

Divirta-se fazendo acústica! Se você experenciar quaisquer _bugs_ ou problemas, tiver sugestões ou ideias,
por favor [abra uma _issue_](https://github.com/jvcarli/femder/issues/new).

Agradecimentos especiais a Luiz Augusto Alvim, Dr. Paulo Mareze, Dr. Eric Brandão, Alexandre Piccini e Rinaldi Petrolli.
