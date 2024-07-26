export class IngredientType {
  name: string;
  price: number;
  gain_estime: number;
  cout_fabrication: number;
  nb_objet: number;
  rentabilite: number;
  quantity: number;

  constructor(
    name: string,
    price: number,
    gain_estime: number,
    cout_fabrication: number,
    nb_object: number,
    rentabilite: number,
    quantity: number
  ) {
    this.name = name;
    this.price = price;
    this.gain_estime = gain_estime;
    this.cout_fabrication = cout_fabrication;
    this.nb_objet = nb_object;
    this.rentabilite = rentabilite;
    this.quantity = quantity;
  }
}
