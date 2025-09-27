using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Metadata.Builders;
using StudentsAffairsWebAPI.Data.Entities;

namespace StudentsAffairsWebAPI.Data.Configurations
{
    public class ApplicantConfiguration : IEntityTypeConfiguration<Applicant>
    {
        public void Configure(EntityTypeBuilder<Applicant> builder)
        {
            builder.ToTable("Applicants");

            builder.HasKey(e => e.Id);
            builder.HasIndex(e => e.Name).IsUnique();

            builder.Property(e => e.Id)
                   .IsRequired()
                   .HasMaxLength(5);

            builder.Property(e => e.Name)
                   .IsRequired()
                   .HasMaxLength(50);

            builder.Property(e => e.Mobile)
                   .HasMaxLength(20);

            builder.Property(e => e.Age)
                   .HasMaxLength(2)
                   .HasDefaultValue(18);
        }
    }
}
