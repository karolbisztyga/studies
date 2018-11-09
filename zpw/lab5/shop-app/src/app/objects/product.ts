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
        public id: number,
        public name: string,
        public quantity: number,
        public price_for_one: number,
        public description: string,
        public img_url: string) {
        }
}