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