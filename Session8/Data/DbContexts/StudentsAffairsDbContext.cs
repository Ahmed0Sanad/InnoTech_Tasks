using Microsoft.EntityFrameworkCore;
using StudentsAffairsWebAPI.Data.Entities;

namespace StudentsAffairsWebAPI.Data.DbContexts
{
    public class StudentsAffairsDbContext : DbContext
    {
        public StudentsAffairsDbContext(DbContextOptions<StudentsAffairsDbContext> options)
            : base(options)
        {
        }

        public DbSet<Student> Students { get; set; }
        public DbSet<Applicant> Applicants { get; set; }

        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            base.OnModelCreating(modelBuilder);

            // Apply all configurations in the assembly
            modelBuilder.ApplyConfigurationsFromAssembly(typeof(ProjectReference).Assembly);
        }
    }
}
