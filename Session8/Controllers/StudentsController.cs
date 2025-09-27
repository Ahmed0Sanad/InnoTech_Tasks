using StudentsAffairsWebAPI.Data.DbContexts;
using StudentsAffairsWebAPI.Data.Entities;
using System.Diagnostics;

namespace StudentsAffairsWebAPI;

[Route("api/[controller]")]
[ApiController]
public class StudentsController : BaseController<Student>
{
    public StudentsController(StudentsAffairsDbContext studentsAffairsDbContext) : base(studentsAffairsDbContext)
    {
    }
}
