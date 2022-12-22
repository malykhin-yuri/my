#!/bin/bash

name=$1.tex
cat > $name <<'HEAD'
\documentclass[12pt]{article}
\usepackage[utf8]{inputenc}
\usepackage[russian]{babel}
\usepackage{amsmath,amssymb,amsthm}
\renewcommand\le{\leqslant}
\renewcommand\ge{\geqslant}
\begin{document}

\end{document}
HEAD
