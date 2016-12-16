#include <stdio.h>
#include <string.h>

void compute_checksum(char* input, char* output, int in_len)
{
    for(int i=0; i<in_len; i=i+2) {
        output[i/2] = (input[i] == input[i+1] ? '1' : '0');
    }
}

int main()
{

    int disc_len = 35651584;
    char disc[disc_len*2];
    memset(disc, 0, sizeof(disc));

    int input_len = 17;
    char input[input_len];
    strncpy(input, "00101000101111010", input_len);
    memcpy(disc, input, input_len);
    
    int curr_len = input_len;
    while(strlen(disc) < disc_len) {
        memset(disc+curr_len, '0', curr_len);
        memcpy(disc+curr_len+1, disc, curr_len);
        for (int i=curr_len+1; i<curr_len+1+(curr_len/2); i++) {
            char swap = disc[i];
            disc[i] = disc[curr_len*2+1+curr_len-i];
            disc[curr_len*2+1+curr_len-i] = swap;
        }
        for (int i=curr_len+1; i<curr_len*2+1; i++) {
            if (disc[i] == '1') { disc[i] = '0'; }
            else if (disc[i] == '0') { disc[i] = '1'; }
            else { printf("Error encountered - copied element not 0 or 1\n"); }
        }
        curr_len = curr_len*2 + 1;
    }
    
    disc[disc_len] = 0;
    
    char checksum[disc_len];
    memset(checksum, 0, disc_len);
    compute_checksum(disc, checksum, disc_len);
    
    while(strlen(checksum) % 2 == 0) {
        disc_len = disc_len / 2;
        char temp[disc_len];
        memset(temp, 0, disc_len);
        compute_checksum(checksum, temp, disc_len);
        strcpy(checksum, temp);
    }
    
}
