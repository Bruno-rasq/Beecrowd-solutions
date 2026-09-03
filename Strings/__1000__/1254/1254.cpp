#include <iostream>
#include <cctype>
using namespace std;

int main(){
    string CURRENT_TAG, TAG_TO_REPLACE, html_code;
    
    while(getline(cin, CURRENT_TAG)){
        getline(cin, TAG_TO_REPLACE);
        getline(cin, html_code);
        bool TAG_FLAG = false;
        string ans = "";
        
        for(size_t i = 0; i < html_code.size(); i++){
            if(html_code[i] == '<') TAG_FLAG = true;
            else if(html_code[i] == '>') TAG_FLAG = false;
            else if(TAG_FLAG)
                if(i < html_code.size() - CURRENT_TAG.size()){
                    bool found = true;
                    for(size_t j = 0; j < CURRENT_TAG.size(); j++){
                        char a = tolower(static_cast<unsigned char>(CURRENT_TAG[j]));
                        char b = tolower(static_cast<unsigned char>(html_code[i + j]));
                        if(a != b){
                            found = false;
                            break;
                        }
                    }
                    if(found){
                        ans += TAG_TO_REPLACE;
                        i += CURRENT_TAG.size() - 1;
                        continue;
                    }
                }
            ans += html_code[i];
        }
        cout << ans << "\n";
    }
}