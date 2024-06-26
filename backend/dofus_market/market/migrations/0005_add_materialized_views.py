# Generated by Django 5.0.6 on 2024-06-28 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0004_alter_ingredient_price'),
    ]

    operations = [
        migrations.RunSQL("""
            CREATE MATERIALIZED VIEW EstimatedGains AS (
            SELECT
                e.name,
                SUM(c.number_of_ra * r.prix_ra + c.number_of_pa * r.prix_pa + c.number_of_ba * r.prix_ba) AS estimated_gain
            FROM market_dofusobject e
            JOIN market_dofusobject__effects ef ON e.name = ef.dofusobject_id
            JOIN market_caracteristique c ON c.id = ef.caracteristique_id
            JOIN market_rune r on r.name = c.rune_id
            GROUP BY e.name
            )
            """),
    
        migrations.RunSQL("""
            CREATE MATERIALIZED VIEW FabricationCosts AS (
            SELECT
                e.name,
                SUM(i.price * if.quantity) * 1.03 AS fabrication_cost
            FROM market_dofusobject e
            JOIN market_dofusobject__ingredients ei ON e.name = ei.dofusobject_id
            JOIN market_ingredientforcraft if ON ei.ingredientforcraft_id = if.id
            JOIN market_ingredient i on if.ingredient_id = i.name
            GROUP BY e.name 
            )
            """),

        migrations.RunSQL("""
            CREATE MATERIALIZED VIEW Rentability AS (
            SELECT
                eg.name,
                COALESCE(eg.estimated_gain, 0) AS equipement_estimated_gain,
                COALESCE(fc.fabrication_cost, 0) AS equipement_fabrication_cost,
                (COALESCE(eg.estimated_gain, 0) - COALESCE(fc.fabrication_cost, 1000000000)) / COALESCE(fc.fabrication_cost, 1) * 100 AS rentability
            FROM EstimatedGains eg
            LEFT JOIN FabricationCosts fc ON eg.name = fc.name
            )
            """),
        migrations.RunSQL("""
            CREATE MATERIALIZED VIEW OrderedByRentability AS ( 
	        SELECT
	            e.name,
	            e.metier_id,
	            r.equipement_estimated_gain,
	            r.equipement_fabrication_cost,
	            r.rentability
	        FROM market_dofusobject e
	        LEFT JOIN Rentability r ON e.name = r.name
	        ORDER BY r.rentability DESC
            )
            """),
    ]
