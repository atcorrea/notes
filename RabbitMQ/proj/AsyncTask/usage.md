## Usage
- 3 Terminais necessários
- Executar na ordem abaixo

### Terminal #1:
```
cd Worker
dotnet run
# => [*] Waiting for messages. To exit press CTRL+C
```
### Terminal #2:
```
cd Worker
dotnet run
# => [*] Waiting for messages. To exit press CTRL+C
```
### Terminal #3:
```
cd ../NewTask
dotnet run "1 message."
dotnet run "2 message.."
dotnet run "3 message..."
dotnet run "4 message...."
dotnet run "5 message....."
dotnet run "6 message......"
...
```