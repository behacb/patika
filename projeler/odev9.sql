--1.
select * from city
inner join country on city.country_id=country.country_id;
--2.
select payment_id,first_name,last_name from customer
inner join payment on customer.customer_id=payment.customer_id;
--3.
SELECT customer.first_name,customer.last_name,rental.rental_id
FROM customer
INNER JOIN rental ON rental.customer_id = customer.customer_id;
