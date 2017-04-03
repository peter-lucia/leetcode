class Solution {
public:
    int binary_string_to_int(std::string num) {
        std::bitset<32> result(num);
        return int(result.to_ulong());
    }
    std::string strip_binary(int n) {
        if (n == 0) {
            return "0";
        }
        std::string bit = std::bitset<32>(n).to_string();
        int index = 0;
        std::string substring;
        for (unsigned int i = 0;i < bit.length(); i++) {
            if(bit[i] == '1') {
                index = i;
                break;
            }
        }
        substring = bit.substr(index);
        return substring;
    }
    int findComplement(int n) {
        if (n == 0) {
            return 1;
        }
        if (n == 1) {
            return 0;
        }
        if (n == 2) {
            return 1;
        }
        if (n == 3) {
            return 0;
        }
        std::bitset<32> num_bin(n);
        std::string test = strip_binary(n);
        int stripped_length = test.length();
        std::bitset<32> complement = ~num_bin;
        std::ostringstream temp;
        temp << complement;
        std::string comp_result = temp.str();
        std::string comp_shortened_result = comp_result.substr(comp_result.length() - stripped_length);
        int result = binary_string_to_int(comp_shortened_result);
        return result;

}

};