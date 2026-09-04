#include <iostream>
#include <unordered_map>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

using solved_problems = int;
using students = vector<string>;
using Hash = unordered_map<solved_problems, students>;

int main()
{
    int qnt_students;
    int instance = 1;

    while (cin >> qnt_students)
    {
        Hash ranked;
        int solved;
        int lowest_solved_count = 10; // valor de 0 a 10
        string student_name;

        for (int i = 0; i < qnt_students; i++)
        {
            cin >> student_name >> solved;
            ranked[solved].push_back(student_name);

            if (solved < lowest_solved_count)
                lowest_solved_count = solved;
        }

        students& lowest_ranked = ranked[lowest_solved_count];
        sort(lowest_ranked.begin(), lowest_ranked.end());

        cout << "Instancia " << instance << endl;
        cout << lowest_ranked.back() << endl << endl;

        instance++;
    }
}