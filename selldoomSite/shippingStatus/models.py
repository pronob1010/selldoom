# from django.db import models
# from seller import models
# # Create your models here.
# class shipping_actions(models.Model):
#     id = models.AutoField(primary_key=True)
#     order_id = models.ForeignKey(product, on_delete=models.CASCADE)
#     product_ready_for_shipping = models.BooleanField(default=False)
#     shipping_text_for_user = models.CharField(max_length=500, null=True)

# class shipping_agent_actions(models.Model):
#     id = models.AutoField(primary_key=True)
#     seller_action_id = models.ForeignKey(product, on_delete=models.CASCADE)
#     product_received = models.BooleanField(default=False)

