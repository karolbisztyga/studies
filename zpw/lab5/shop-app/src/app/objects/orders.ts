import { Product } from "./product";

export class Order {
    constructor(
        public id: number = 0,
        public address: string = "",
        public products: Product[] = [],
        public totalPrice: number = 0,
        public date: string = '',
        public status: string = 'waiting',
        public key:string = '') {
            // status can be 'waiting' or 'done'
        }
}