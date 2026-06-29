# Structure-de-donnee-tri-colis

# 📦 Mini Projet — Algorithmes & Structures de Données

Projet réalisé dans le cadre du cursus DA2I — Semestre S3/S4.

## 📋 Description

Simulation d'un **centre de tri de colis** mettant en œuvre les structures
de données fondamentales et les algorithmes de tri classiques.

Le système modélise le flux réel d'un centre logistique :
- Les colis arrivent et entrent dans une **file d'attente** (FIFO)
- Ils sont ensuite transférés vers une **pile de chargement** (LIFO)
- Différents algorithmes de tri permettent d'ordonner les colis

## 🏗️ Architecture du projet
├── main.py          # Point d'entrée — classe CentreTri et menu interactif

├── structures.py    # Implémentation FileAttente (FIFO) et PileChargement (LIFO)

├── colis.py         # Modèle Colis + générateur aléatoire

└── tris.py          # Algorithmes de tri (insertion & sélection)

## 🧠 Structures de données implémentées

| Structure | Type | Usage |
|-----------|------|-------|
| `FileAttente` | FIFO | Réception des colis entrants |
| `PileChargement` | LIFO | Chargement vers le camion |

## ⚙️ Algorithmes de tri

| Algorithme | Complexité | Stable | Appliqué sur |
|------------|-----------|--------|--------------|
| Tri par insertion | O(n²) / O(n) meilleur cas | ✅ Oui | File (par priorité) |
| Tri par sélection | O(n²) tous les cas | ❌ Non | File & Pile (par poids) |

## 🚀 Installation & Exécution

```bash
# Cloner le repo
git clone https://github.com/Mohamadou2/data-structures-sorting.git
cd data-structures-sorting

# Lancer le programme (Python 3 requis, aucune dépendance externe)
python main.py
```

## 🖥️ Fonctionnalités

- ➕ Ajout manuel ou aléatoire de colis (destinations mauritaniennes)
- 🔄 Transfert File → Pile → Camion
- 📊 Tri de la file par **priorité** (1 à 5)
- ⚖️ Tri de la pile par **poids**
- 📈 Comparaison des performances des algorithmes

## 👤 Auteur

**Mamadou Abou Ba** — Étudiant DA2I  
🔗 [GitHub](https://github.com/Mohamadou2) · [LinkedIn](https://www.linkedin.com/in/mamadou-abou-ba-6433432a3)
