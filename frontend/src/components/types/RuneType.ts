export class RuneType {
  name: string;
  prixRa: number;
  prixPa: number;
  prixBa: number;

  constructor(name: string, prix_ra: number, prix_pa: number, prix_ba: number) {
    this.name = name;
    this.prixRa = prix_ra;
    this.prixPa = prix_pa;
    this.prixBa = prix_ba;
  }
}
