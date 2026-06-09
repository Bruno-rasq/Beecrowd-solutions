#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;

const double GRAVITY = 9.80665;
const double PI      = 3.14159;

struct Angular_velocity { double VX, VY; };

double parse_graus_to_radius(double graus){ return graus * (PI / 180.0); }

Angular_velocity decompose_velocity(double speed, double angle){
    double rad = parse_graus_to_radius(angle);
    double vx = speed * cos(rad);
    double vy = speed * sin(rad);
    return {vx, vy};
}

/*
    y(t) = alturainticial + (vy * t) - (gravidade/2) * t²
    onde t é o tempo que objeto permanece no ar.
    
    y(t) = 0, significa que objeto regressou ao solo.
*/
double duration_on_air(const Angular_velocity& Vel, double height){
    double a = -(GRAVITY / 2.0);
    double b = Vel.VY;
    double c = height;
    double delta = b*b - 4*a*c;
    double t1 = (-b + sqrt(delta)) / (2*a);
    double t2 = (-b - sqrt(delta)) / (2*a);
    return max(t1, t2);
}

double distance_traveled(const Angular_velocity& Vel, double temp){
    return Vel.VX * temp;
}

int main() {
    int p1, p2, attempts;
    double height, angle, speed;
    
    while(cin >> height){
        cin >> p1 >> p2 >> attempts;
        while(attempts--){
            cin >> angle >> speed;
            
            Angular_velocity vel = decompose_velocity(speed, angle);
            double temp = duration_on_air(vel, height);
            double range = distance_traveled(vel, temp);
            
            cout << fixed << setprecision(5) << range;
            
            // acertou a area do alvo.
            if(range >= (float)p1 && range <= (float)p2){
                cout << " -> DUCK\n";
                continue;
            }
            cout << " -> NUCK\n";
        }
    }
}