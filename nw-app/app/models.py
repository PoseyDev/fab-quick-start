from sqlalchemy import Boolean, Column, DECIMAL, DateTime, Float, ForeignKey, Integer, LargeBinary, String, UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()  # from sqlacodegen
metadata = Base.metadata


class Category(Base):
    __tablename__ = 'Category'

    Id = Column(Integer, primary_key=True)
    CategoryName = Column(String(8000))
    Description = Column(String(8000))


class Customer(Base):
    __tablename__ = 'Customer'

    Id = Column(String(8000), primary_key=True)
    CompanyName = Column(String(8000))
    ContactName = Column(String(8000))
    ContactTitle = Column(String(8000))
    Address = Column(String(8000))
    City = Column(String(8000))
    Region = Column(String(8000))
    PostalCode = Column(String(8000))
    Country = Column(String(8000))
    Phone = Column(String(8000))
    Fax = Column(String(8000))


class CustomerDemographic(Base):
    __tablename__ = 'CustomerDemographic'

    Id = Column(String(8000), primary_key=True)
    CustomerDesc = Column(String(8000))


class Employee(Base):
    __tablename__ = 'Employee'

    Id = Column(Integer, primary_key=True)
    LastName = Column(String(8000))
    FirstName = Column(String(8000))
    Title = Column(String(8000))
    TitleOfCourtesy = Column(String(8000))
    BirthDate = Column(String(8000))
    HireDate = Column(String(8000))
    Address = Column(String(8000))
    City = Column(String(8000))
    Region = Column(String(8000))
    PostalCode = Column(String(8000))
    Country = Column(String(8000))
    HomePhone = Column(String(8000))
    Extension = Column(String(8000))
    Photo = Column(LargeBinary)
    Notes = Column(String(8000))
    ReportsTo = Column(Integer)
    PhotoPath = Column(String(8000))


class Product(Base):
    __tablename__ = 'Product'

    Id = Column(Integer, primary_key=True)
    ProductName = Column(String(8000))
    SupplierId = Column(Integer, nullable=False)
    CategoryId = Column(Integer, nullable=False)
    QuantityPerUnit = Column(String(8000))
    UnitPrice = Column(DECIMAL, nullable=False)
    UnitsInStock = Column(Integer, nullable=False)
    UnitsOnOrder = Column(Integer, nullable=False)
    ReorderLevel = Column(Integer, nullable=False)
    Discontinued = Column(Integer, nullable=False)


class Region(Base):
    __tablename__ = 'Region'

    Id = Column(Integer, primary_key=True)
    RegionDescription = Column(String(8000))


class Shipper(Base):
    __tablename__ = 'Shipper'

    Id = Column(Integer, primary_key=True)
    CompanyName = Column(String(8000))
    Phone = Column(String(8000))


class Supplier(Base):
    __tablename__ = 'Supplier'

    Id = Column(Integer, primary_key=True)
    CompanyName = Column(String(8000))
    ContactName = Column(String(8000))
    ContactTitle = Column(String(8000))
    Address = Column(String(8000))
    City = Column(String(8000))
    Region = Column(String(8000))
    PostalCode = Column(String(8000))
    Country = Column(String(8000))
    Phone = Column(String(8000))
    Fax = Column(String(8000))
    HomePage = Column(String(8000))


class Territory(Base):
    __tablename__ = 'Territory'

    Id = Column(String(8000), primary_key=True)
    TerritoryDescription = Column(String(8000))
    RegionId = Column(Integer, nullable=False)


class AbPermission(Base):
    __tablename__ = 'ab_permission'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)


class AbRegisterUser(Base):
    __tablename__ = 'ab_register_user'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(64), nullable=False)
    last_name = Column(String(64), nullable=False)
    username = Column(String(64), nullable=False, unique=True)
    password = Column(String(256))
    email = Column(String(64), nullable=False)
    registration_date = Column(DateTime)
    registration_hash = Column(String(256))


class AbRole(Base):
    __tablename__ = 'ab_role'

    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False, unique=True)


class AbUser(Base):
    __tablename__ = 'ab_user'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(64), nullable=False)
    last_name = Column(String(64), nullable=False)
    username = Column(String(64), nullable=False, unique=True)
    password = Column(String(256))
    active = Column(Boolean)
    email = Column(String(64), nullable=False, unique=True)
    last_login = Column(DateTime)
    login_count = Column(Integer)
    fail_login_count = Column(Integer)
    created_on = Column(DateTime)
    changed_on = Column(DateTime)
    created_by_fk = Column(ForeignKey('ab_user.id'))
    changed_by_fk = Column(ForeignKey('ab_user.id'))

    parent = relationship('AbUser', remote_side=[id], primaryjoin='AbUser.changed_by_fk == AbUser.id')
    parent1 = relationship('AbUser', remote_side=[id], primaryjoin='AbUser.created_by_fk == AbUser.id')


class AbViewMenu(Base):
    __tablename__ = 'ab_view_menu'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False, unique=True)


class CustomerCustomerDemo(Base):
    __tablename__ = 'CustomerCustomerDemo'

    Id = Column(String(8000), primary_key=True)
    CustomerTypeId = Column(ForeignKey('Customer.Id'))

    Customer = relationship('Customer')


class EmployeeTerritory(Base):
    __tablename__ = 'EmployeeTerritory'

    Id = Column(String(8000), primary_key=True)
    EmployeeId = Column(ForeignKey('Employee.Id'), nullable=False)
    TerritoryId = Column(ForeignKey('Territory.Id'))

    Employee = relationship('Employee')
    Territory = relationship('Territory')


class Order(Base):
    __tablename__ = 'Order'

    Id = Column(Integer, primary_key=True)
    CustomerId = Column(ForeignKey('Customer.Id'))
    EmployeeId = Column(Integer, nullable=False)
    OrderDate = Column(String(8000))
    RequiredDate = Column(String(8000))
    ShippedDate = Column(String(8000))
    ShipVia = Column(Integer)
    Freight = Column(DECIMAL, nullable=False)
    ShipName = Column(String(8000))
    ShipAddress = Column(String(8000))
    ShipCity = Column(String(8000))
    ShipRegion = Column(String(8000))
    ShipPostalCode = Column(String(8000))
    ShipCountry = Column(String(8000))

    Customer = relationship('Customer')


class AbPermissionView(Base):
    __tablename__ = 'ab_permission_view'
    __table_args__ = (
        UniqueConstraint('permission_id', 'view_menu_id'),
    )

    id = Column(Integer, primary_key=True)
    permission_id = Column(ForeignKey('ab_permission.id'))
    view_menu_id = Column(ForeignKey('ab_view_menu.id'))

    permission = relationship('AbPermission')
    view_menu = relationship('AbViewMenu')


class AbUserRole(Base):
    __tablename__ = 'ab_user_role'
    __table_args__ = (
        UniqueConstraint('user_id', 'role_id'),
    )

    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey('ab_user.id'))
    role_id = Column(ForeignKey('ab_role.id'))

    role = relationship('AbRole')
    user = relationship('AbUser')


class OrderDetail(Base):
    __tablename__ = 'OrderDetail'

    Id = Column(String(8000), primary_key=True)
    OrderId = Column(ForeignKey('Order.Id'), nullable=False)
    ProductId = Column(ForeignKey('Product.Id'), nullable=False)
    UnitPrice = Column(DECIMAL, nullable=False)
    Quantity = Column(Integer, nullable=False)
    Discount = Column(Float, nullable=False)

    Order = relationship('Order')
    Product = relationship('Product')


class AbPermissionViewRole(Base):
    __tablename__ = 'ab_permission_view_role'
    __table_args__ = (
        UniqueConstraint('permission_view_id', 'role_id'),
    )

    id = Column(Integer, primary_key=True)
    permission_view_id = Column(ForeignKey('ab_permission_view.id'))
    role_id = Column(ForeignKey('ab_role.id'))

    permission_view = relationship('AbPermissionView')
    role = relationship('AbRole')
