#include <stdio.h>
#include <string.h>
#include <WinSock2.h>

#pragma comment(lib, "ws2_32.lib")

#define BUF_SIZE    1024

void ErrorHandling(char * errmsg);

int main(int argc, char ** argv)
{
	WSADATA wsaData;
	SOCKET sock;
	SOCKADDR_IN servAddr;
	char buf[BUF_SIZE];
	int strLen = 0;
	int recvLen = 0;
	int recvCnt;

	if (argc != 3)
	{
		printf("usage : %s <IP> <port> \n", argv[0]);
		exit(-1);
	}

	if (WSAStartup(MAKEWORD(2, 2), &wsaData) != 0)
		ErrorHandling("WSAStartup() error!");

	sock = socket(PF_INET, SOCK_STREAM, 0);
	if (sock == INVALID_SOCKET)
		ErrorHandling("socket() error!");

	memset(&servAddr, 0, sizeof(servAddr));
	servAddr.sin_family = AF_INET;
	servAddr.sin_addr.s_addr = inet_addr(argv[1]);
	servAddr.sin_port = htons(atoi(argv[2]));

	if (connect(sock, (SOCKADDR*)&servAddr, sizeof(servAddr)) == SOCKET_ERROR)
		ErrorHandling("connect() error!");

	while (1)
	{
		gets(buf); strLen = strlen(buf)+1;
		if (!strcmp(buf, "q") || !strcmp(buf, "Q"))
			return 0;

		send(sock, buf, strLen, 0);

		recvLen = 0;
		while (recvLen < strLen)
		{
			recvCnt = recv(sock, buf, strLen, 0);
			if (recvCnt == -1)
				ErrorHandling("recv() error!");
			recvLen += recvCnt;
		}
		printf("message from server : %s \n", buf);
	}
	closesocket(sock);
	WSACleanup();
	return 0;
}

void ErrorHandling(char * errmsg)
{
	fputs(errmsg, stderr);
	fputc('\n', stderr);
	exit(-1);
}
