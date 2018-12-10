export class Product {
    constructor(
        public id: number = 0,
        public name: string = "",
        public quantity: number = 0,
        public price_for_one: number = 0,
        public description: string = "",
        public img_url: string = "",
        public categories: string[] = [],
        public total_price: number = 0,
        public price: number = 0,
        public key: string = '') {
            this.total_price = this.price_for_one
        }
}