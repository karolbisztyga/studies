/*
interface ProductInterface {
    id: number;
    name: string;
    quantity: number;
    price_for_one: number;
    description: string;
    img_url: string;
}
*/
export class Product {
    constructor(
        public id: number = 0,
        public name: string = "",
        public quantity: number = 0,
        public price_for_one: number = 0,
        public description: string = "",
        public img_url: string = "") {
        }
}