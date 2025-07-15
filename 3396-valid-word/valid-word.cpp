class Solution {
public:
    bool isValid(string word) {
        if(word.size()<3) return false;
        bool vowel=false;
        bool consonant=false;
        for(auto i:word){
            if(i>=97 && i<=122){
                if(i=='a' || i=='e' || i=='o' || i=='i' || i=='u'){
                    vowel=true;
                }
                else{
                    consonant=true;
                }
            }
            else if(i>=65 && i<=90){
                if(i=='A' || i=='E' || i=='I' || i=='O' || i=='U'){
                    vowel=true;
                }
                else{
                    consonant=true;
                }
            }
            else if(i>=48 && i<=57){
                continue;
            }
            else{
                return false;
            }
        }
        return vowel&consonant;
    }
};