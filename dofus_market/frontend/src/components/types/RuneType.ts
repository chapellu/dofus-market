export class RuneType {
  name: string;
  prix_ra: number;
  prix_pa: number;
  prix_ba: number;

  constructor(name: string, prix_ra: number, prix_pa: number, prix_ba: number) {
    this.name = name;
    this.prix_ra = prix_ra;
    this.prix_pa = prix_pa;
    this.prix_ba = prix_ba;
  }
}
