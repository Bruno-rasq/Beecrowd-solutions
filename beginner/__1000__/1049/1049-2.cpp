#include <iostream>
#include <unordered_map>
using namespace std;

template<typename K, typename V>
using UM = unordered_map<K, V>;

int main() {

    UM<string, UM<string, UM<string, string>>> graph;

    graph["vertebrado"]["ave"]["carnivoro"] = "aguia";
    graph["vertebrado"]["ave"]["onivoro"] = "pomba";
    graph["vertebrado"]["mamifero"]["onivoro"] = "homem";
    graph["vertebrado"]["mamifero"]["herbivoro"] = "vaca";
    graph["invertebrado"]["inseto"]["hematofago"] = "pulga";
    graph["invertebrado"]["inseto"]["herbivoro"] = "lagarta";
    graph["invertebrado"]["anelideo"]["hematofago"] = "sanguessuga";
    graph["invertebrado"]["anelideo"]["onivoro"] = "minhoca";
    
    string key1, key2, key3;
    cin >> key1 >> key2 >> key3;

    cout << graph[key1][key2][key3] << "\n";
}