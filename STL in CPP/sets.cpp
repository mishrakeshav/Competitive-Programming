#include<iostream>
#include<set>
#include<string>
#include<functional>
using namespace std;

class Person{
    public:
        float age;
        string name;
    bool operator < (const Person& rhs) const { return age < rhs.age; };
    bool operator > (const Person& rhs) const { return age > rhs.age; };

};

int main(){
    std::set<int> Set = {5,4,3,2,1};
    for(int i : Set){
        cout << i << endl;
    }

    set<Person, std::greater<>> persons = {{19, "Keshav"}, {20, "Jaideep"}, {21, "Kanha"}};
    for(Person p : persons){
        cout << p.age << " "<<p.name << endl;
    }
    return 0;
}