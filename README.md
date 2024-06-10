# dofus-market

```mermaid
---
title: Dofus market
---
classDiagram
    class DofusObject {
        string name
        int level
        string metier
    }

    class Ingredient {
        string name
        int prix
    }

    class IngredientForCraft {
        int quantity
    }

    class Statistique {
        int min
        int max
    }

    class Caracteristique {
        string name
    }

    class Rune {
        string name
        int prix_ra
        int prix_pa
        int prix_ba
    }

    DofusObject "1" -- "*" IngredientForCraft

    DofusObject "*" -- "*" Statistique

    IngredientForCraft "*" -- "1" Ingredient

    Caracteristique "1" -- "1" Rune

    Statistique "*" -- "1" Caracteristique



```

---

```mermaid
---
title: Dofus market
---
classDiagram
    class Equipement {
        string name
        int level
    }

    class Metier {
        string name
    }

    class Ingredient {
        string name
        int prix
    }

    class IngredientForCraft {
        int quantity
    }

    class Statistique {
        int min
        int max
        float ra
        float pa
        float ra
    }

    class Caracteristique {
        string name
    }

    class Rune {
        string name
        int prix_ra
        int prix_pa
        int prix_ba
    }

    class Recette {
        int level
    }




    Equipement "*" -- "*" IngredientForCraft

    Equipement "1" -- "*" Statistique

    IngredientForCraft "*" -- "1" Ingredient

    Caracteristique "1" -- "1" Rune

    Statistique "*" -- "1" Caracteristique

    Equipement "*" -- "1" Metier

    Recette "*" -- "1" Metier

    Recette "1" -- "*" IngredientForCraft

    Recette "0..1" -- "" Ingredient

```


|name|level|metierForeignKey|
|----|---|---|
|Bottes du boufton|2|metier1|
**Table 1:** Equipement

|name|
|----|
|Cordonnier|
**Table 2:** Metier

|objetForeignKey|CaractéristiqueForeignKey|jetMin|jetMax|Ra|Pa|Ba|
|----|---|---|--|--|--|--|
|equipement1|caracteristique1|3|5|0.0|0.0|1.2|
**Table 3:** Statistique

|name|runeForeignKey|
|--|--|
|Agilité|rune1|
**Table 4:** Caracterisitque

|name|prixRa|prixPa|prixBa|
|--|--|--|--|
|Age|xx|xx|xx|
**Table 5:** Rune

|equipementForeignKey|ingredientForeignKey|quantity|
|--|--|--|
|equipement1|ingredient1|1|
|equipement1|ingredient2|1|
**Table 6:** IngredientForCraft

|name|price|
|--|--|
|Fleur de lin|12|
|bois de frenes|5|
**Table 7:** Ingredient
