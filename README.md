# sfeGroup6
creating a project

#include <iostream>
#include <stdlib.h>

using namespace std;

char board[3][3] = {{'1','2','3'},{'4','5','6'},{'7','8','9'}};

int choice;
int row,column;
char turn = 'X';
bool draw = false;

void display(){


    cout << "PLAYER - 1 [X]t PLAYER - 2 [O]nn";
    cout << "     |     |     ";
    cout << "  "<< board[0][0] << "  | "<< board[0][1] << "  |  " << board[0][2] << " n" << endl;
    cout << "_____|_____|_____";
    cout << "     |     |     ";
    cout << "  " << board[1][0] << "  | "<< board[1][1] << "  |  " << board[1][2] << " n" << endl;
    cout << "_____|_____|_____";
    cout << "     |     |     "; 
    cout << "  "<< board[2][0] << "  | "<< board[2][1] << "  |  " << board[2][2] << " n" << endl;
    cout << "     |     |     ";
}


void player_turn(){
    if(turn == 'X'){
        cout<<"Player - 1 [X] turn : ";
    }
    else if(turn == 'O'){
        cout<<"Player - 2 [O] turn : ";
    }
    cin>> choice;

    switch(choice){
        case 1: row = 0; column = 0; break;
        case 2: row = 0; column = 1; break;
        case 3: row = 0; column = 2; break;
        case 4: row = 1; column = 0; break;
        case 5: row = 1; column = 1; break;
        case 6: row = 1; column = 2; break;
        case 7: row = 2; column = 0; break;
        case 8: row = 2; column = 1; break;
        case 9: row = 2; column = 2; break;
        default:
            cout << "Invalid Move" << endl;
    }

    if(turn == 'X' && board[row][column] != 'X' && board[row][column] != 'O'){
        
        board[row][column] = 'X';
        turn = 'O';
    }
	else if(turn == 'O' && board[row][column] != 'X' && board[row][column] != 'O'){
        
        board[row][column] = 'O';
        turn = 'X';
    }
	else {
        cout << "Box already filled, choose another" << endl;
        player_turn();
    }
    display();
}


bool gameover(){
    
    for(int i=0; i <= 3; i++)
    if(board[i][0] == board[i][1] && board[i][0] == board[i][2] || board[0][i] == board[1][i] && board[0][i] == board[2][i])
    return false;


    if(board[0][0] == board[1][1] && board[0][0] == board[2][2] || board[0][2] == board[1][1] && board[0][2] == board[2][0])
    return false;

    for(int i=0; i < 3; i++){
    for(int j=0; j < 3; j++)
    if(board[i][j] != 'X' && board[i][j] != 'O')
    return true;
	}

    draw = true;
    return false;
}


int main()
{
    cout << "T I C K -- T A C -- T O E -- G A M E";
    
    while(gameover())
	{
        display();
        player_turn();
        gameover();
    }
    if(turn == 'X' && draw == false)
	{
        cout << "Congratulations. Player with X has won the game";
    }
    else if(turn == 'O' && draw == false)
	{
        cout << "Congratulations. Player with O has won the game";
    }
    else
    cout << "DRAW!" << endl;
	
	return 0;
}[tic tac toeee2.txt](https://github.com/PercyLech/sfeGroup6/files/6833278/tic.tac.toeee2.txt)
