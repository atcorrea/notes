using System;
using RabbitMQ.Client;
using RabbitMQ.Client.Events;
using System.Text;
using System.Threading;

namespace Worker
{
    class Worker
    {
        static void Main(string[] args)
        {
            var factory = new ConnectionFactory() {HostName = "localhost"};
            using (var connection = factory.CreateConnection())
            {
                using (var channel = connection.CreateModel())
                {
                    channel.QueueDeclare(queue: "task_queue", durable: false, exclusive: false, autoDelete: false, arguments: null);

                    var consumer = new EventingBasicConsumer(channel);
                    consumer.Received += (model, ea) => {
                        var body = ea.Body.ToArray();
                        var message = Encoding.UTF8.GetString(body);
                        Console.WriteLine($"[X] received: {message}");

                        var dots = message.Split(".").Length -1;
                        Thread.Sleep(dots * 1000);

                        Console.WriteLine("[X] Done");
                    };

                    channel.BasicConsume(queue: "task_queue", autoAck: true, consumer: consumer);     

                    Console.WriteLine("[*] Waiting for messages. To exit press CTRL+C");
                    Console.ReadKey();               
                }                
            }                        
        }
    }
}
