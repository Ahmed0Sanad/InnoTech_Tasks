using FluentValidation;

namespace BlazorAppStandAlone.Validators;

public class StudentValidator : AbstractValidator<Student>
{
    public StudentValidator()
    {
        RuleFor(x => x.Name)
            .NotEmpty()
            .WithMessage("Name is required")
            .Length(2, 100)
            .WithMessage("Name must be between 2 and 100 characters");

        RuleFor(x => x.Mobile)
            .NotEmpty()
            .WithMessage("Mobile is required")
            .Matches(@"^(\+20|0)?1[0-2,5]\d{8}$")
            .WithMessage("Please enter a valid Egyptian mobile number");

        RuleFor(x => x.Telephone)
            .NotEmpty()
            .WithMessage("Telephone is required")
            .Matches(@"^(\+20|0)?[2-9]\d{7,8}$")
            .WithMessage("Please enter a valid telephone number");

        RuleFor(x => x.Email)
            .NotEmpty()
            .WithMessage("Email is required")
            .EmailAddress()
            .WithMessage("Please enter a valid email address")
            .Length(5, 100)
            .WithMessage("Email must be between 5 and 100 characters");

        RuleFor(x => x.Age)
            .NotEmpty()
            .WithMessage("Age is required")
            .InclusiveBetween(16, 120)
            .WithMessage("Age must be between 16 and 120 years");

        RuleFor(x => x.Message)
            .NotEmpty()
            .WithMessage("Message is required")
            .Length(10, 500)
            .WithMessage("Message must be between 10 and 500 characters");
    }
}
