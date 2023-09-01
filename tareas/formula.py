using System;

namespace CalculadoraDeArea
{
    class Program
    {
        static void Main(string[] args)
        {
            // Pedir al usuario que ingrese el radio del círculo
            Console.Write("Ingrese el radio del círculo: ");
            double radio = Convert.ToDouble(Console.ReadLine());

            // Calcular el área del círculo
            double area = Math.PI * Math.Pow(radio, 2);

            // Mostrar el resultado
            Console.WriteLine($"El área del círculo con radio {radio} es {area}");

            // Esperar a que el usuario presione una tecla para salir
            Console.ReadKey();
        }
    }
}
