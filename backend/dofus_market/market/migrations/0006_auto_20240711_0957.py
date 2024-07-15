# Generated by Django 5.0.6 on 2024-07-11 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0005_add_materialized_views'),
    ]

    operations = [
        migrations.RunSQL("""
        DROP MATERIALIZED VIEW OrderedByRentability
        """),
        migrations.RunSQL("""
        CREATE MATERIALIZED VIEW OrderedByRentability AS ( 
	        SELECT
	            e.name,
                e.level,
	            e.metier_id,
                COUNT(ei.dofusobject_id) AS number_of_ingredients,
	            r.equipement_estimated_gain,
	            r.equipement_fabrication_cost,
	            r.rentability
	        FROM market_dofusobject e
            Left JOIN market_dofusobject__ingredients ei ON e.name = ei.dofusobject_id
	        LEFT JOIN Rentability r ON e.name = r.name
            GROUP BY e.name, e.level, e.metier_id, r.equipement_estimated_gain, r.equipement_fabrication_cost, r.rentability
	        ORDER BY r.rentability DESC
            )
        """)
    ]
