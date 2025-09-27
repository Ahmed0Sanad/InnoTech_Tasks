using System.ComponentModel.DataAnnotations;
namespace BlazorAppStandAlone;

public class Student
{
    public Guid Id { get; set; }

    [Required(ErrorMessage = "Name is required")]
    public string? Name { get; set; }

    [Required(ErrorMessage = "Mobile is required")]
    public string? Mobile { get; set; }

    [Required(ErrorMessage = "Telephone is required")]

    public string? Telephone { get; set; }

    [Required(ErrorMessage = "Email is required")]
    [EmailAddress(ErrorMessage = "Invalid email address")]
    public string? Email { get; set; }

    [Required(ErrorMessage = "Age is required")]
    public int Age { get; set; }

    [Required(ErrorMessage = "Message is required")]
    public string? Message { get; set; }
}
