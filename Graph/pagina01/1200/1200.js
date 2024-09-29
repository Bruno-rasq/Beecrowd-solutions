const fs = require("fs")
const input = fs.readFileSync("/dev/stdin", "utf-8")
const lines = input.split("\n")

class Node {
    constructor(data, left = null, right = null){
        this.data = data
        this.left = left
        this.right = right
    }
}

class BST { // binary search tree

    constructor(){
        this.root = null
    }

    add(data){
        const node = new Node(data)

        if(this.root == null){
            this.root = node
        } else {

            const searchNode = (current) => {
                if(data < current.data){
                    if(current.left === null){
                        current.left = node
                        return
                    } else {
                        return searchNode(current.left)
                    }
                } else if (data > current.data){
                    if(current.right === null){
                        current.right = node
                        return
                    } else {
                        return searchNode(current.right)
                    }
                } else {
                    return null
                }
            }

            return searchNode(this.root)
        }

    }

    search(data){
        const searchNode = (current) => {

            if(current === null) return false

            if(data < current.data){
                return searchNode(current.left)
            }

            if(data > current.right){
                return searchNode(current.right)
            }

            return true
        }

        console.log(searchNode(this.root) ? `${data} existe` : `${data} nao existe`)
    }

    InOrder(){
        if(this.root === null) return null

        const nodelist =  []
        const Transverse = (current) => {
            if(current.left) Transverse(current.left)
            nodelist.push(current.data)
            if(current.right) Transverse(current.right)
        }

        Transverse(this.root)
        console.log(nodelist.join(' '))
    }

    PreOrder(){
        if(this.root === null) return null

        const nodelist =  []
        const Transverse = (current) => {
            nodelist.push(current.data)
            if(current.left) Transverse(current.left)
            if(current.right) Transverse(current.right)
        }

        Transverse(this.root)
        console.log(nodelist.join(' '))
    }

    PosOrder(){
        if(this.root === null) return null

        const nodelist =  []
        const Transverse = (current) => {
            if(current.left) Transverse(current.left)
            if(current.right) Transverse(current.right)
            nodelist.push(current.data)
        }

        Transverse(this.root)
        console.log(nodelist.join(' '))
    }
}


let bst = new BST()

for(let i = 0; i < lines.length; i++){
    let curr = lines[i].trim()

    if(curr == "INFIXA") bst.InOrder()
    if(curr == "PREFIXA") bst.PreOrder()
    if(curr == "POSFIXA") bst.PosOrder()

    if(curr != "INFIXA" || curr != "PREFIXA" || curr != "POSFIXA" && curr != ""){
        let [action, data] = curr.split(" ")

        if(action == "I" && data){
            bst.add(data)

        } else if(action == "P" && data){
            bst.search(data)
        }
    }
}