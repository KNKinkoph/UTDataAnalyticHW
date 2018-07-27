Sub Easy():

'Setting Data Type

    Dim Name As String
    Dim Value As Double
    Dim i As Double
    Dim j As Double
    
'Defining variables (row in which value will begin)
    j = 2
    i = 2
    
'Defining Labels for new columns

    Cells(1, 9).Value = "Ticker"
    Cells(1, 10).Value = "Total Volume"
    
'Creating Loops - j + 1 and i = i + 1 to continue to move through row


Do While Cells(j, 1) <> ""
    Name = "Cells(j, 1).Value"
    Value = 0
    
        Do While Cells(j, 1).Value = Name
            Value = Value + Cells(j, 7).Value
            j = j + 1
        Loop
        
    Cells(i, 9).Value = Name
    Cells(i, 10).Value = Value
        
    i = i + 1
Loop
End Sub