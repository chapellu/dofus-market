import { IngredientType } from "./IngredientType";

export class EquipementType {
  name: string;
  rentabilite: number;
  cout_fabrication: number;
  gain_estime: number;
  nb_objet: number;
  ingredients: [IngredientType];

  constructor(
    name: string,
    rentabilite: number,
    cout_fabrication: number,
    gain_estime: number,
    nb_objet: number,
    ingredients: [IngredientType]
  ) {
    this.name = name;
    this.rentabilite = rentabilite;
    this.ingredients = ingredients;
    this.cout_fabrication = cout_fabrication;
    this.gain_estime = gain_estime;
    this.nb_objet = nb_objet;
  }
}
