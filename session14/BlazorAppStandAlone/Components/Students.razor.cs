namespace BlazorAppStandAlone.Components;
using System.Text.Json;
public partial class Students
{
    private Student student = new();
    List<Student> students = new List<Student>();
    protected async override Task OnAfterRenderAsync(bool firstRender)
    {
        await base.OnAfterRenderAsync(firstRender);
        //TODO:: using HttpClient call https://students.innopack.app/api/students to fill students
        if (firstRender && !students.Any())
        {
            student.Id = Guid.NewGuid();
            student.Name = "Wael Shehab Eldin";
            student.Mobile = "01207888335";
            student.Telephone = "0403335102";
            student.Email = "wael@innotech.com.eg";
            student.Age = 44;
            student.Message = "Just Testing......";

            StateHasChanged();
        }
    }

    private void HandleValidSubmit()
    {
        string studentSerialized = JsonSerializer.Serialize(student);
        Student? validStudent = JsonSerializer.Deserialize<Student>(studentSerialized);
        if (validStudent is not null)
            students.Add(validStudent);
        //Search With name if exits get it by index and edit it in list if not add it to list
        //TODO:: using HttpClient call https://students.innopack.app/api/students
    }
    private void EditStudent(Student toBeEditedStudent)
    {
        student = toBeEditedStudent;

        StateHasChanged();
    }

    public class ContactModel
    {

        public string? Name { get; set; }


        public string? Email { get; set; }


    }
}