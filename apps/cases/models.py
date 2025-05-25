from django.db import models
from apps.histories.models import Histories
# Create your models here.

class Cases(models.Model):
    description = models.TextField(verbose_name="Description")
    priority = models.CharField(max_length=20, verbose_name="Priority")
    preconditions = models.TextField(verbose_name="Preconditions")
    input_data = models.TextField(verbose_name="Input Data")
    steps = models.TextField(verbose_name="Steps")
    expected_result = models.TextField(verbose_name="Expected Result")
    actual_result = models.TextField(verbose_name="Actual Result", null=True, blank=True)
    test_status = models.BooleanField(verbose_name="Test Status", null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True, verbose_name="Created At")
    updated_at = models.DateField(auto_now_add=True, verbose_name="Updated At")
    id_us = models.ForeignKey(Histories, on_delete=models.CASCADE, verbose_name="User Story")

    def __str__(self):
        return f'{self.id_us} - {self.description}'

    class Meta:
        verbose_name = 'Test Case'
        verbose_name_plural = 'Test Cases'
        ordering = ['id']