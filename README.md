# 📊 Prédiction de la Fidélité Client & Détection du Churn

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Power BI](https://img.shields.io/badge/Power_BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![Data Science](https://img.shields.io/badge/Data-Science-blue?style=for-the-badge)

## 🎯 Objectif du Projet
L'objectif principal de ce projet est d'analyser le comportement des clients afin de **prédire leur fidélité** et de **détecter en amont les profils à risque de désabonnement (churn)**. Cette approche permet de mettre en place des actions de rétention ciblées.

---

## 🚀 Fonctionnalités Clés
* **Préparation & Analyse des Données :** Nettoyage, exploration et ingénierie des caractéristiques (*Feature Engineering*) d'un dataset client avec Python.
* **Modélisation Prédictive :** Entraînement et comparaison de plusieurs algorithmes de Machine Learning.
* **Visualisation d'Impact :** Création d'un tableau de bord interactif pour l'interprétation business des résultats.

---

## 🧪 Modélisation & Performances

Trois modèles principaux ont été implémentés et évalués :
1. **Régression Logistique** (Baseline)
2. **Random Forest**
3. **XGBoost**

### 🏆 Meilleurs Résultats (Modèle Final)
Le modèle le plus performant (XGBoost) a atteint les scores suivants :
* **Précision (Precision) :** `85 %` — Faible taux de fausses alertes.
* **Rappel (Recall) :** `80 %` — Excellente capacité à capter les clients réels à risque.

---

## 📊 Visualisations & Business Intelligence
Les résultats du modèle ainsi que les indicateurs clés (KPIs) de l'attrition client ont été intégrés et mis en forme via **Power BI**. 
* Analyse des facteurs principaux du Churn.
* Segmentation des profils clients à risque.

---

## 🛠️ Outils & Technologies Utilisés

* **Manipulation des données :** Pandas, NumPy
* **Machine Learning :** Scikit-Learn (Logistic Regression, Random Forest), XGBoost
* **Visualisation :** Matplotlib, Seaborn, Power BI
* **Environnement :** Jupyter Notebook, GitHub Desktop