import datetime

# Liste de lampes frontales (exemple)
lampes = [
    {"nom": "Frontale A", "lumens": 1000, "autonomie_h": 10, "poids_g": 150, "lien": "#"},
    {"nom": "Frontale B", "lumens": 800, "autonomie_h": 15, "poids_g": 120, "lien": "#"},
    {"nom": "Frontale C", "lumens": 1200, "autonomie_h": 8, "poids_g": 180, "lien": "#"},
    {"nom": "Frontale D", "lumens": 600, "autonomie_h": 20, "poids_g": 100, "lien": "#"},
    {"nom": "Frontale E", "lumens": 900, "autonomie_h": 12, "poids_g": 130, "lien": "#"},
]

# Trier pour différents critères
top_lumens = sorted(lampes, key=lambda x: x["lumens"], reverse=True)[:3]
top_autonomie = sorted(lampes, key=lambda x: x["autonomie_h"], reverse=True)[:3]
top_leger = sorted(lampes, key=lambda x: x["poids_g"])[:3]

# Chemin du fichier Hugo
fichier_md = r"C:\Users\Drakax\Desktop\TestAmazon\content\posts\frontales-usbc.md"

# Générer le contenu Markdown
date_aujourdhui = datetime.date.today().isoformat()
contenu = f"""---
title: "Top 3 lampes frontales USB-C (2025)"
date: {date_aujourdhui}
draft: false
---

Voici une sélection de **lampes frontales USB-C** idéales pour la randonnée et le trail :

## Top 3 selon la puissance (lumens)
"""
for lampe in top_lumens:
    contenu += f"- [{lampe['nom']}]({lampe['lien']}) – {lampe['lumens']} lumens, {lampe['autonomie_h']}h, {lampe['poids_g']}g\n"

contenu += "\n## Top 3 selon l'autonomie\n"
for lampe in top_autonomie:
    contenu += f"- [{lampe['nom']}]({lampe['lien']}) – {lampe['lumens']} lumens, {lampe['autonomie_h']}h, {lampe['poids_g']}g\n"

contenu += "\n## Top 3 selon le poids\n"
for lampe in top_leger:
    contenu += f"- [{lampe['nom']}]({lampe['lien']}) – {lampe['lumens']} lumens, {lampe['autonomie_h']}h, {lampe['poids_g']}g\n"

contenu += "\n\n💡 En tant que Partenaire Amazon, je réalise un bénéfice sur les achats remplissant les conditions requises.\n"

# Écrire dans le fichier
with open(fichier_md, "w", encoding="utf-8") as f:
    f.write(contenu)

print("Article mis à jour avec le Top 3/Top 5 des frontales !")
