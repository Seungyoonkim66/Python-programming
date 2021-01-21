#include <sys/stat.h>
#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define BUF_SIZE 1024

int main(int argc, char *argv[])
{
    int inputFd, outputFd, openFlags;
    mode_t filePerms;
    __ssize_t numRead;
    char buf[BUF_SIZE];

    if(argc != 3 || strcmp(argv[1], "--help")==0)
        printf("%s old-file new-file \n", argv[0]);

    inputFd = open(argv[1], O_RDONLY);
    if(inputFd == -1)
        printf("ERROR: opening file %s", argv[1]);

    openFlags =  O_CREAT | O_WRONLY | O_TRUNC;
    filePerms = S_IRUSR | S_IWUSR | S_IRGRP | S_IWGRP | S_IROTH | S_IWOTH;

    outputFd = open(argv[2], openFlags, filePerms);
    if(inputFd == -1)
        printf("ERROR: opening file %s", argv[2]);

    while ((numRead = read(inputFd, buf, BUF_SIZE)) >0 ){
        if (write(outputFd, buf, numRead)!=numRead)
            printf("couldn't write whole buffer");
    }
    if (numRead == -1)
        printf("ERROR : reading file is %s", argv[1]);

    if (close(inputFd) == -1)  
        printf("ERROR : closing input file descriptor");
    
    if (close(outputFd) == -1)  
        printf("ERROR : closing input file descriptor");

    exit(0);

}