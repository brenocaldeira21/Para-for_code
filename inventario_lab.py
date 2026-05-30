# Dados do inventário físico (cada índice representa um frasco individual)
reagentes = [
    'Etanol', 'Acetona', 'Etanol', 'Ácido Sulfúrico', 'Benzeno', 'Acetona',
    'Etanol', 'Ácido Sulfúrico', 'Metanol', 'Tolueno', 'Etanol', 'Acetona',
    'Ácido Acético', 'Etanol', 'Benzeno', 'Ácido Sulfúrico', 'Metanol',
    'Ácido Acético', 'Etanol', 'Acetona', 'Tolueno', 'Ácido Sulfúrico',
    'Benzeno', 'Etanol', 'Acetona', 'Metanol', 'Ácido Sulfúrico', 'Acetona',
    'Ácido Acético', 'Etanol'
]

lotes = [
    '2023-ETA-01', '2023-ACE-01', '2023-ETA-01', '2023-SUL-01',
    '2023-BEN-01', '2024-ACE-01', '2023-ETA-02', '2024-SUL-01', '2023-MET-01',
    '2024-TOL-01', '2023-ETA-01', '2023-ACE-01', '2023-ACA-01', '2023-ETA-02',
    '2023-BEN-01', '2023-SUL-01', '2023-MET-01', '2024-ACA-01', '2023-ETA-01',
    '2023-ACE-01', '2024-TOL-01', '2024-SUL-01', '2023-BEN-01', '2023-ETA-01',
    '2023-ACE-01', '2023-MET-01', '2023-SUL-01', '2024-ACE-01', '2024-ACA-01',
    '2023-ETA-02'
]

purezas = [
    99.5, 92.0, 99.5, 98.0, 99.9, 98.5, 96.0, 99.0, 99.0, 98.8,
    99.5, 92.0, 99.2, 96.0, 99.9, 98.0, 99.0, 95.0, 99.5, 92.0,
    98.8, 99.0, 99.9, 99.5, 92.0, 99.0, 98.0, 98.5, 95.0, 96.0
] 

# PASSO 1 — Identificação dos Tipos de Reagentes (Set)

tipos_unicos = set(reagentes)

print("=" * 65)
print("PASSO 1 — REAGENTES ÚNICOS NO ESTOQUE")
print("=" * 65)
print(f"Total de tipos diferentes: {len(tipos_unicos)}")
print(f"Compostos disponíveis: {tipos_unicos}\n")

# PASSO 1.2 — Estruturação do Inventário (Zip)
inventario = list(zip(reagentes, lotes, purezas))

# PASSO 2 — Geração de Relatório (Unpacking)
print("=" * 65)
print("PASSO 2 — RELATÓRIO COMPLETO DO INVENTÁRIO")
print("=" * 65)
for reagente, lote, pureza in inventario:
    print(f"Frasco do Lote: {lote} | Reagente: {reagente} | Pureza: {pureza}%")
print("=" * 65)

# PASSO 3 — Filtragem por Critério de Qualidade (List Comprehension)
lotes_aprovados = [lote for reagente, lote, pureza in inventario if pureza >= 98.0]

print(f"\nPASSO 3 — LOTES APROVADOS (pureza ≥ 98.0%):")
print(f"{lotes_aprovados}")
print(f"\nTotal de frascos aprovados: {len(lotes_aprovados)}")
