
const fs = require("fs")
const input = fs.readFileSync("/dev/stdin", "utf-8")
const lines = input.split("\n")

class No {
    constructor(
        public data: string,
        public left: No | null = null,
        public right: No | null = null
    ) {}
}

class BST {
    constructor(
        public root: No | null = null
    ) {}

    public add(data: string): void {
        const node = new No(data);

        if (this.root == null) {
            this.root = node;
        } else {
            const searchNode = (current: No) => {
                if (data < current.data) {
                    if (current.left === null) {
                        current.left = node;
                    } else {
                        return searchNode(current.left);
                    }
                } else if (data > current.data) {
                    if (current.right === null) {
                        current.right = node;
                    } else {
                        return searchNode(current.right);
                    }
                }
            };

            searchNode(this.root);
        }
    }

    public search(data: string): void {
        const searchNode = (current: No | null): boolean => {
            if (current === null) return false;

            if (data < current.data) {
                return searchNode(current.left);
            } else if (data > current.data) {
                return searchNode(current.right);
            }

            return true;
        };

        const found: boolean = searchNode(this.root);
        console.log(found ? `${data} existe` : `${data} nao existe`);
    }

    public InOrder(): void {
        if (this.root === null) return;

        const nodelist: string[] = [];
        const Transverse = (current: No) => {
            if (current.left) Transverse(current.left);
            nodelist.push(current.data);
            if (current.right) Transverse(current.right);
        };

        Transverse(this.root);
        console.log(nodelist.join(' '));
    }

    public PreOrder(): void {
        if (this.root === null) return;

        const nodelist: string[] = [];
        const Transverse = (current: No) => {
            nodelist.push(current.data);
            if (current.left) Transverse(current.left);
            if (current.right) Transverse(current.right);
        };

        Transverse(this.root);
        console.log(nodelist.join(' '));
    }

    public PosOrder(): void {
        if (this.root === null) return;

        const nodelist: string[] = [];
        const Transverse = (current: No) => {
            if (current.left) Transverse(current.left);
            if (current.right) Transverse(current.right);
            nodelist.push(current.data);
        };

        Transverse(this.root);
        console.log(nodelist.join(' '));
    }
}

let bst = new BST();

for (let i = 0; i < lines.length; i++) {
    let curr = lines[i].trim();

    if (curr === "INFIXA") bst.InOrder();
    else if (curr === "PREFIXA") bst.PreOrder();
    else if (curr === "POSFIXA") bst.PosOrder();
    else {
        let [action, data] = curr.split(" ");

        if (action === "I" && data) {
            bst.add(data);
        } else if (action === "P" && data) {
            bst.search(data);
        }
    }
}
