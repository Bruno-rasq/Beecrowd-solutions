#include <iostream>
#include <unordered_map>
using namespace std;

int main() {

    unordered_map<string, string> graph;

    graph["vertebrado ave carnivoro"] = "aguia\n";
    graph["vertebrado ave onivoro"] = "pomba\n";
    graph["vertebrado mamifero onivoro"] = "homem\n";
    graph["vertebrado mamifero herbivoro"] = "vaca\n";
    graph["invertebrado inseto hematofago"] = "pulga\n";
    graph["invertebrado inseto herbivoro"] = "lagarta\n";
    graph["invertebrado anelideo hematofago"] = "sanguessuga\n";
    graph["invertebrado anelideo onivoro"] = "minhoca\n";
    
    string key1, key2, key3;
    cin >> key1 >> key2 >> key3;

    cout << graph[key1 + " " + key2 + " " + key3];
}